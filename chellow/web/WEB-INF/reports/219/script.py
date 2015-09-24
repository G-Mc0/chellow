from net.sf.chellow.monad import Monad
import datetime
import pytz
from dateutil.relativedelta import relativedelta
from sqlalchemy import or_, and_
import traceback
import utils
import db

Monad.getUtils()['impt'](globals(), 'utils', 'db')

HH, hh_format = utils.HH, utils.hh_format
RegisterRead, Bill, Supply, Era = db.RegisterRead, db.Bill, db.Supply, db.Era
inv = globals()['inv']

year = inv.getInteger("end_year")
month = inv.getInteger("end_month")
months = inv.getInteger("months")
if inv.hasParameter('supply_id'):
    supply_id = inv.getLong('supply_id')
else:
    supply_id = None


def content():
    sess = None
    try:
        sess = db.session()

        finish_date = datetime.datetime(year, month, 1, tzinfo=pytz.utc) + \
            relativedelta(months=1) - HH

        start_date = datetime.datetime(year, month, 1, tzinfo=pytz.utc) - \
            relativedelta(months=months-1)

        reads = sess.query(RegisterRead).filter(
            or_(
                and_(
                    RegisterRead.present_date >= start_date,
                    RegisterRead.present_date <= finish_date),
                and_(
                    RegisterRead.previous_date >= start_date,
                    RegisterRead.previous_date <= finish_date))) \
            .join(Bill).order_by(Bill.supply_id)

        if supply_id is not None:
            supply = Supply.get_by_id(sess, supply_id)
            reads = reads.filter(Bill.supply == supply)

        yield "Duration Start,Duration Finish,Supply Id,Import MPAN Core," \
            "Export MPAN Core,Batch Reference,Bill Id,Bill Reference," \
            "Bill Issue Date,Bill Type,Register Read Id,TPR,Coefficient," \
            "Previous Read Date,Previous Read Value,Previous Read Type," \
            "Present Read Date,Present Read Value,Present Read Type\n"

        for read in reads:
            bill = read.bill
            supply = bill.supply
            batch = bill.batch

            era = supply.find_era_at(sess, bill.start_date)
            if era is None:
                eras = sess.query(Era).filter(
                    Era.supply_id == supply.id).order_by(Era.start_date).all()
                if bill.start_date < eras[0].start_date:
                    era = eras[0]
                else:
                    era = eras[-1]

            yield ','.join(
                '"' + ('' if val is None else str(val)) + '"' for val in [
                    hh_format(start_date), hh_format(finish_date), supply.id,
                    era.imp_mpan_core, era.exp_mpan_core, batch.reference,
                    bill.id, bill.reference, hh_format(bill.issue_date),
                    bill.bill_type.code, read.id,
                    'md' if read.tpr is None else read.tpr.code,
                    read.coefficient, hh_format(read.previous_date),
                    read.previous_value, read.previous_type.code,
                    hh_format(read.present_date), read.present_value,
                    read.present_type.code]) + '\n'
    except:
        yield traceback.format_exc()
    finally:
        if sess is not None:
            sess.close()

file_name = 'reads_' + \
    datetime.datetime.now(pytz.utc).strftime("%Y%M%d%H%m") + '.csv'
utils.send_response(inv, content, file_name=file_name)