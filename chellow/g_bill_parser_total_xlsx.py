from dateutil.relativedelta import relativedelta
import openpyxl
from collections import defaultdict
from itertools import islice
from chellow.utils import HH, to_utc
from decimal import Decimal


def to_money(cell):
    return round(Decimal(cell.value), 2)


class Parser():
    def __init__(self, f):
        self.book = openpyxl.load_workbook(filename=f)
        self.sheet = self.book.get_sheet_by_name('Report')
        self.rows = tuple(self.sheet.rows)

        self.titles = ','.join(
            c.value for c in self.rows[0] if c.value is not None)
        self._line_number = None

    @property
    def line_number(self):
        return None if self._line_number is None else self._line_number + 2

    def _set_last_line(self, line):
        self.last_line = line
        return line

    def make_raw_bills(self):
        raw_bills = []
        last_bill_reference = None
        raw_bill = None
        for self._line_number, row in enumerate(self.rows[1:]):
            if row[0].value is None:
                continue
            bill_reference = str(row[8].value)
            if last_bill_reference != bill_reference:
                breakdown = defaultdict(int, {'gas_rate': set()})
                raw_bill = {
                    'reference': bill_reference, 'reads': [], 'kwh': 0,
                    'breakdown': breakdown, 'net_gbp': Decimal('0.00'),
                    'vat_gbp': Decimal('0.00'), 'gross_gbp': Decimal('0.00'),
                    'raw_lines': self.titles + '\n'}
                raw_bills.append(raw_bill)
                last_bill_reference = bill_reference
            if row[9].value is None:
                raw_bill['account'] = row[5].value
                raw_bill['issue_date'] = row[6].value
                if row[7].value is None:
                    raw_bill['bill_type_code'] = 'N'
                else:
                    raw_bill['bill_type_code'] = 'W'

                raw_bill['msn'] = row[9].value
                raw_bill['mprn'] = str(row[10].value)
                raw_bill['start_date'] = to_utc(row[17].value)
                raw_bill['finish_date'] = to_utc(row[18].value) + \
                    relativedelta(days=1) - HH
                breakdown['vat_5pc'] += row[28].value
                breakdown['vat_15pc'] += row[29].value
                breakdown['vat_17_5pc'] += row[30].value
                breakdown['vat_20pc'] += row[31].value
                raw_bill['vat_gbp'] += to_money(row[32])
                raw_bill['breakdown']['standing_gbp'] = row[33].value
                raw_bill['gross_gbp'] += to_money(row[34])
                raw_bill['raw_lines'] += ','.join(
                    str(c.value) for c in islice(row, 35)) + '\n'
                raw_bill['net_gbp'] += raw_bill['gross_gbp'] - \
                    raw_bill['vat_gbp']
            else:
                read = {
                    'msn': row[9].value,
                    'mprn': str(row[10].value),
                    'prev_value': row[11].value,
                    'prev_date': to_utc(row[12].value),
                    'prev_type_code': row[13].value[-1],
                    'pres_value': row[14].value,
                    'pres_date': to_utc(row[15].value),
                    'pres_type_code': row[16].value[-1],
                    'correction_factor': row[20].value,
                    'calorific_value': row[21].value,
                    'units': row[25].value}
                vat_gbp = to_money(row[32])
                gross_gbp = to_money(row[34])
                raw_bill['reads'].append(read)
                raw_bill['kwh'] += row[22].value
                raw_bill['net_gbp'] += gross_gbp - vat_gbp
                raw_bill['vat_gbp'] += vat_gbp
                raw_bill['gross_gbp'] += gross_gbp
                raw_bill['raw_lines'] += ','.join(
                    str(c.value) for c in islice(row, 35)) + '\n'
                breakdown['gas_rate'].add(row[23].value)
                breakdown['units_consumed'] += row[24].value
                breakdown['gas_gbp'] += row[26].value
                breakdown['ccl_gbp'] += row[27].value
                breakdown['vat_5pc'] += row[28].value
                breakdown['vat_15pc'] += row[29].value
                breakdown['vat_17_5pc'] += row[30].value
                breakdown['vat_20pc'] += row[31].value
        for raw_bill in raw_bills:
            breakdown = raw_bill['breakdown']
            if len(breakdown['gas_rate']) == 1:
                breakdown['gas_rate'] = breakdown['gas_rate'].pop()
            else:
                breakdown['gas_rate'] = ''
            raw_bill['breakdown'] = dict(breakdown)
        return raw_bills
