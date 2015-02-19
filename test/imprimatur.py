[
    # Users
    {
        'name': "Manipulating users",
        'port': '5000',
        'host': 'localhost',
        'path': '/chellow/reports/255/output/',
        'method': 'post',
        'auth': ('admin@example.com', 'admin'),
        'data': {
            'email_address': "watkins@example.com",
            'user_role_code': "editor",
            'password': "alan", },
        'status_code': 303,
        'regexes': [
            r"/reports/257/output/\?user_id=2", ], },
    {
        'path': '/chellow/reports/255/output/',
        'method': 'post',
        'data': {
            'email_address': "lydgate@localhost",
            'user_role_code': "editor",
            'password': "science", },
        'status_code': 303,
        'regexes': [
            r"/reports/257/output/\?user_id=3", ], },
    {
        'path': '/chellow/reports/257/output/?user_id=3',
        'regexes': [
            r'<input type="hidden" name="user_id" value="3">\s*'
            '<legend>Delete this user</legend>', ],
        'status_code': 200, },

    # Check that a duplicate email gives a proper error message
    {
        'path': '/chellow/reports/255/output/',
        'method': 'post',
        'data': {
            'email_address': "lydgate@localhost",
            'user_role_code': "editor",
            'password': "science", },
        'regexes': [
            r"already a user with this email address", ],
        'status_code': 400, },

    # Test that we're able to change the password
    {
        'path': '/chellow/reports/257/output/',
        'method': 'post',
        'data': {
            'user_id': "3",
            'current_password': "science",
            'new_password': "rosamund",
            'confirm_new_password': "rosamund", },
        'status_code': 303, },

    # Test that we can change the role
    {
        'path': '/chellow/reports/257/output/',
        'method': 'post',
        'data': {
            'user_id': "3",
            'email_address': "mary-ann-evans@example.com",
            'user_role_code': "editor", },
        'status_code': 303, },

    # ...and change it back
    {
        'path': '/chellow/reports/257/output/',
        'method': 'post',
        'data': {
            'user_id': "3",
            'email_address': "lydgate@localhost",
            'user_role_code': "editor", },
        'status_code': 303, },
    {
        'name': "Check that invalid email address gives unauthorized.",
        'path': '/chellow/reports/315/output/',
        'method': 'post',
        'auth': ('godel', 'dancer'),
        'data': {
            'participant_id': "222",

            # HYDE
            'name': "Non half-hourlies 2007",
            'start_year': "2000",
            'start_month': "01",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00",
            'has_finished': "false", },
        'status_code': 401, },
    {
        'name': "Check duplicate report name gives good error message",
        'path': '/chellow/reports/',
        'method': 'post',
        'auth': ('watkins@example.com', 'alan'),
        'data': {
            'name': "Home", },
        'status_code': 400,
        'regexes': [
            r"There's already a report with that name\.", ], },

    # Valid },
    {
        'name': "site",
        'path': '/chellow/reports/293/output/',
        'method': 'post',
        'files': {'import_file': 'sites.csv'},
        'status_code': 303,
        'regexes': [
            r"/reports/295/output/\?process_id=0", ], },
    {
        'path': '/chellow/reports/295/output/?process_id=0',
        'tries': {'max': 10, 'period': 1},
        'status_code': 200,
        'regexes': [
            r"The file has been imported successfully\.", ], },

    # duplicates
    {
        'path': '/chellow/reports/293/output/',
        'method': 'post',
        'files': {'import_file': 'sites.csv'},
        'status_code': 303,
        'regexes': [
            r"/reports/295/output/\?process_id=1", ], },
    {
        'path': '/chellow/reports/295/output/?process_id=1',
        'tries': {'max': 10, 'period': 1},
        'regexes': [
            r"There&#39;s already a site with this code\.", ],
        'status_code': 200, },

    # Delete a site
    {
        'path': '/chellow/reports/311/output/',
        'method': 'post',
        'data': {
            'site_id': "2",
            'delete': "Delete", },
        'status_code': 303, },

    # Show and and add a site
    {
        'path': '/chellow/reports/297/output/',
        'regexes': [
            r"Add a site", ],
        'status_code': 200, },
    {
        'path': '/chellow/reports/297/output/',
        'method': 'post',
        'data': {
            'code': "CH017",
            'name': "Parbola", },
        'status_code': 303, },
    {
        'name': "HHDC contracts",
        'path': '/chellow/reports/277/output/',
        'method': 'post',
        'data': {
            'participant_id': "61",  # DASL
            'name': "HH contract",
            'start_year': "2000",
            'start_month': "01",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00",
            'has_finished': "false", },
        'status_code': 303,
        'regexes': [
            r"/reports/115/output/\?hhdc_contract_id=53", ], },

    # Update Contract
    {
        'path': '/chellow/reports/279/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "53",
            'party_id': "97",  # DASL HHDC
            'name': "HH contract",
            'charge_script': """
def virtual_bill_titles():
    return ['net-gbp', 'problem']

def virtual_bill(supply_source):
    supply_source.dc_bill['net-gbp'] = 0
""",
            'properties': "{'mpan_map': {'maptest': '2292056799106'}}", },
        'status_code': 303, },
    {
        'path': '/chellow/reports/279/output/?hhdc_contract_id=53',
        'regexes': [
            r"HH contract", ],
        'status_code': 200, },

    # Check that we can see HHDC rate script okay. Contract 53.
    {
        'path': '/chellow/reports/173/output/?hhdc_rate_script_id=305',

        # Check that 'has_finished' field is there
        'regexes': [
            r"HH contract", ],
        'status_code': 200, },

    # Check that we can see the edit view of the HHDC rate script okay.
    # Contract 53.
    {
        'path': '/chellow/reports/249/output/?hhdc_rate_script_id=305',

        # Check that 'has_finished' field is there
        'regexes': [
            r"has_finished",

            # Check the hhdc_rate_script_id for update is there
            r'<legend>Update Rate Script</legend>\s*'
            '<input type="hidden" name="hhdc_rate_script_id"\s*'
            'value="305">', ],
        'status_code': 200, },

    # Check that we can update an HHDC rate script okay
    {
        'path': '/chellow/reports/249/output/',
        'method': 'post',
        'data': {
            'hhdc_rate_script_id': "305",
            'start_year': "2000",
            'start_month': "01",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00",
            'script': "{}", },
        'status_code': 303, },

    # Add another HHDC contract
    {
        'path': '/chellow/reports/277/output/',
        'method': 'post',
        'data': {
            'participant_id': "61",  # DASL
            'name': "Dynamat data",
            'start_year': "2000",
            'start_month': "01",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00", },
        'status_code': 303,
        'regexes': [
            r"/reports/115/output/\?hhdc_contract_id=54", ], },

    # Update the newly added HHDC
    {
        'path': '/chellow/reports/279/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "54",
            'party_id': "97",  # DASL HHDC
            'name': "Dynamat data",
            'charge_script': """
def virtual_bill_titles():
    return ['net-gbp', 'problem']

def virtual_bill(supply_source):
    supply_source.dc_bill['net-gbp'] = 0
""",
            'properties': '{"props": 1}', },
        'status_code': 303, },

    # Update state of Dynamat HHDC
    {
        'path': '/chellow/reports/279/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "54",
            'update_state': "",
            'state': '{"stat": 2}', },
        'status_code': 303, },

    # View Dynamat HHDC
    {
        'path': '/chellow/reports/279/output/?hhdc_contract_id=54',
        'status_code': 200,
        'regexes': [
            r'<textarea name="charge_script" rows="40" cols="80">\s*'
            'def virtual_bill_title',
            r'<textarea name="properties" rows="40" '
            'cols="80">\{&#34;props&#34;: 1\}</textarea>',
            r'<textarea name="state" rows="40" cols="80">'
            '\{&#34;stat&#34;: 2\}</textarea>', ], },
    {
        'name': "Check one can update the participant for an HHDC contract.",
        'path': '/chellow/reports/279/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "54",
            'party_id': "651",

            # UKDC
            'name': "Dynamat data",
            'start_year': "2000",
            'start_month': "01",
            'start_day': "03",
            'has_finished': "false",
            'charge_script': """
def virtual_bill_titles():
    return ['net-gbp', 'problem']

def virtual_bill(supply_source):
    supply_source.dc_bill['net-gbp'] = 0
""",
            'properties': "{}", },
        'status_code': 303, },

    # Check it's still there
    {
        'path': '/chellow/reports/279/output/?hhdc_contract_id=54',
        'status_code': 200,
        'regexes': [
            r'option value="651" selected', ], },

    # Check correct fields present for adding a supplier contract },
    {
        'name': "Manipulate supplier contracts",
        'path': '/chellow/reports/315/output/',
        'regexes': [
            r'name="start_year"', ],
        'status_code': 200, },

    # Create a new supplier contract
    {
        'path': '/chellow/reports/315/output/',
        'method': 'post',
        'data': {
            'participant_id': "28",  # BIZZ
            'name': "Half-hourlies 2007",
            'start_year': "2000",
            'start_month': "01",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00",
            'charge_script': "",
            'properties': "{'hydrogen': 'sonata'}", },
        'regexes': [
            r"/reports/77/output/\?supplier_contract_id=55", ], },

    # Check that it's displayed properly
    {
        'path': '/chellow/reports/317/output/?supplier_contract_id=55',
        'regexes': [
            r'<option value="22" selected>',
            r'<textarea name="properties" rows="20" '
            'cols="80">\{&#39;hydrogen&#39;: &#39;sonata&#39;\}</textarea>', ],
        'status_code': 200, },
    {
        'path': '/chellow/reports/77/output/?supplier_contract_id=55',
        'regexes': [
            r'<legend>Download Displaced Virtual Bills</legend>\s*<br/>\s*'
            'For <input name="months" value="1" maxlength="2" size="2">\s*'
            'month\(s\) until the end of\s*'
            '<input name="finish_year" maxlength="4" size="4" '
            'value="201\d">', ],
        'status_code': 200, },

    # Update the associated rate script. Supplier contract 55
    {
        'path': '/chellow/reports/319/output/',
        'method': 'post',
        'data': {
            'supplier_rate_script_id': "307",
            'start_year': "2000",
            'start_month': "01",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00",
            'has_finished': "false",
            'script': """
def gsp_gbp_per_kwh():
    return {
        'winter-pk': 0.0193918,
        'winter-low-pk': 0.0501474,
        'winter-off-pk': 0.0062656,
        'summer-pk': 0.0062656,
        'night': 0.0062656,
        'other': 0.0062656}
""", },
        'status_code': 303, },

    # Create a new non-core contract },
    {
        'name': "Manipulate non-core contracts",
        'path': '/chellow/reports/265/output/',
        'method': 'post',
        'data': {
            'participant_id': "31",

            # CALB
            'is_core': "false",
            'name': "VAT",
            'start_year': "2000",
            'start_month': "01",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00", },
        'regexes': [
            r"/chellow/reports/267/output/\?non_core_contract_id=56", ],
        'status_code': 303, },

    # Update the new non-core contract
    {
        'path': '/chellow/reports/269/output/',
        'method': 'post',
        'data': {
            'non_core_contract_id': "56",
            'name': "VAT 2",
            'start_year': "2000",
            'start_month': "01",
            'start_day': "03",
            'charge_script': """import sys

def totalElement(account, startDate, finishDate):
    return ["total", 22.3, "VAT cost"]
""",
            'properties': "{}", },
        'status_code': 303, },
    {
        'path': '/chellow/reports/267/output/?non_core_contract_id=56',
        'regexes': [
            r"import sys\s*def", ],
        'status_code': 200, },

    # Delete it
    {
        'path': '/chellow/reports/269/output/',
        'method': 'post',
        'data': {
            'non_core_contract_id': "56",
            'delete': "", },
        'status_code': 303, },
    {
        'name': "Insert MOP contract",
        'path': '/chellow/reports/361/output/',
        'method': 'post',
        'data': {
            'participant_id': "409",  # LENG
            'name': "MOP Contract",
            'start_year': "2000",
            'start_month': "01",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00", },
        'status_code': 303,
        'regexes': [
            r"/reports/107/output/\?mop_contract_id=57", ], },

    # Update with a charge script
    {
        'path': '/chellow/reports/151/output/',
        'method': 'post',
        'data': {
            'mop_contract_id': "57",
            'party_id': "690",  # LENG
            'name': "MOP Contract",
            'start_year': "2000",
            'start_month': "01",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00",
            'charge_script': """
def virtual_bill_titles():
    return ['net-gbp', 'problem']

def virtual_bill(ds):
    bill = ds.mop_bill
    bill['net-gbp'] = 0
""",
            'properties': "{}", },
        'status_code': 303,
        'regexes': [
            r"/reports/107/output/\?mop_contract_id=57", ], },

    # Check we can see the rate scripts
    {
        'path': '/chellow/reports/107/output/?mop_contract_id=57',
        'status_code': 200, },

    # Insert a modern supplier contract
    {
        'name': "Insert a modern supplier contract. Create a new supplier "
        "contract for 2013",
        'path': '/chellow/reports/315/output/',
        'method': 'post',
        'data': {
            'participant_id': "54",  # COOP
            'name': "Half-hourlies 2013",
            'start_year': "2013",
            'start_month': "01",
            'start_day': "01",
            'start_hour': "00",
            'start_minute': "00",
            'charge_script': "",
            'properties': "{}", },
        'regexes': [
            r"/chellow/reports/77/output/\?supplier_contract_id=58", ],
        'status_code': 303, },

    # Update the associated rate script. Supplier contract 58
    {
        'path': '/chellow/reports/319/output/',
        'method': 'post',
        'data': {
            'supplier_rate_script_id': "310",
            'start_year': "2000",
            'start_month': "01",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00",
            'has_finished': "false",
            'script': """
def gsp_gbp_per_kwh():
    return {
        'winter-pk': 0.0193918,
        'winter-low-pk': 0.0501474,
        'winter-off-pk': 0.0062656,
        'summer-pk': 0.0062656,
        'night': 0.0062656,
        'other': 0.0062656}
""", },
        'status_code': 303, },

    # Create a new supplier contract
    {
        'path': '/chellow/reports/315/output/',
        'method': 'post',
        'data': {
            'participant_id': "386",  # HYDE
            'name': "Non half-hourlies 2007",
            'start_year': "2000",
            'start_month': "01",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00",
            'has_finished': "false",
            'charge_script': "",
            'properties': "{}", },
        'regexes': [
            r"/reports/77/output/\?supplier_contract_id=59", ],
        'status_code': 303, },

    # Give proper error if there are too few fields },
    {
        'name': "supplies",
        'path': '/chellow/reports/293/output/',
        'method': 'post',
        'files': {'import_file': 'supplies-too-few-fields.csv'},
        'regexes': [
            r"/reports/295/output/\?process_id=2", ],
        'status_code': 303, },
    {
        'path': '/chellow/reports/295/output/?process_id=2',
        'tries': {'max': 10, 'period': 1},
        'regexes': [
            r"Another field called Supply Name needs to be added on the end",
        ],
        'status_code': 200, },

    # non-existent source code
    {
        'path': '/chellow/reports/293/output/',
        'method': 'post',
        'files': {'import_file': 'supplies_source.csv'},
        'regexes': [
            r"/reports/295/output/\?process_id=3", ],
        'status_code': 303, },
    {
        'path': '/chellow/reports/295/output/?process_id=3',
        'tries': {'max': 10, 'period': 1},

        # check that it knows that the first line has a source code that is too
        # long
        'regexes': [
            r"There&#39;s no source with the code &#39;netlong&#39;", ],
        'status_code': 200, },

    # Line 2 has a DNO that doesn't exist
    {
        'path': '/chellow/reports/293/output/',
        'method': 'post',
        'files': {'import_file': 'supplies_dno.csv'},
        'regexes': [
            r"/reports/295/output/\?process_id=4", ],
        'status_code': 303, },
    {
        'path': '/chellow/reports/295/output/?process_id=4',
        'tries': {},

        # check that it knows that line 2 has a DNO that doesn't exist
        'regexes': [
            r"There isn&#39;t a DNO contract with the code &#39;79&#39;\.", ],
        'status_code': 200, },

    # Check that it gives a sensible error message if a data is malformed
    {
        'path': '/chellow/reports/293/output/',
        'method': 'post',
        'files': {'import_file': 'supplies_date.csv'},
        'regexes': [
            r"/chellow/reports/295/output/\?process_id=5", ],
        'status_code': 303, },
    {
        'path': '/chellow/reports/295/output/?process_id=5',
        'tries': {'max': 10, 'period': 1},

        # check that it knows that line 1 has a malformed date
        'regexes': [
            r"Can&#39;t parse the date: 2003-0/\*\*d8/03. It needs to be of "
            "the form yyyy-mm-dd hh:MM. invalid literal for int\(\) with base "
            "10: ", ],
        'status_code': 200, },

    # Check for a sensible error message if the site doesn't exist
    {
        'path': '/chellow/reports/293/output/',
        'method': 'post',
        'files': {'import_file': 'supplies_no_site.csv'},
        'regexes': [
            r"/chellow/reports/295/output/\?process_id=6", ],
        'status_code': 303, },
    {
        'path': '/chellow/reports/295/output/?process_id=6',
        'tries': {'max': 10, 'period': 1},

        # check that it knows that line 1 has a malformed date
        'regexes': [
            r"There isn&#39;t a site with the code zzznozzz\.", ],
        'status_code': 200, },

    # Valid import of supplies
    {
        'path': '/chellow/reports/293/output/',
        'method': 'post',
        'files': {'import_file': 'supplies.csv'},
        'status_code': 303,
        'regexes': [
            r"/reports/295/output/\?process_id=7", ], },
    {
        'path': '/chellow/reports/295/output/?process_id=7',
        'tries': {'max': 10, 'period': 1},

        # Check it's loaded ok
        'regexes': [
            r"The file has been imported successfully", ],
        'status_code': 200, },

    # Check that a supply with only an import MPAN is there
    {
        'path': '/chellow/reports/311/output/?site_id=4',
        'regexes': [
            r"22 6354 2983 570",

            # Check we the 'site_id' field is there
            r'<fieldset>\s*<input type="hidden" name="site_id" value="4">\s*'
            '<legend>Update this site</legend>', ],
        'status_code': 200, },

    # Can we see a site ok?
    {
        'path': '/chellow/reports/311/output/?site_id=1',

        # Is the era displayed?
        'regexes': [
            r"<tr>\s*<td>2003-08-03 00:00</td>\s*<td>Ongoing</td>\s*"
            "<td>gen</td>\s*<td>2</td>\s*<td>\s*</td>\s*<td>\s*"
            "22 7907 4116 080\s*</td>\s*</tr>",

            # Does it show the import MPAN?
            r"22 9813 2107 763", ],
        'status_code': 200, },

    # Can we see a supply ok? },

    # View a supply in edit mode
    {
        'name': "view a supply",
        'path': '/chellow/reports/305/output/?supply_id=2',

        # Check table of existing eras is there
        'regexes': [
            r"<table>\s*<caption>Existing Eras</caption>",

            # Check reference to ongoing era
            r"<td>2003-08-03 00:00</td>\s*<td>\s*Ongoing", ],
        'status_code': 200, },
    {
        'path': '/chellow/reports/305/output/',
        'method': 'post',

        # Can we update a supply name?

        # Can we update a supply source?
        'data': {
            'supply_id': "1",
            'name': "Hello",
            'source_id': "4",
            'generator_type_id': "1",
            'gsp_group_id': "11", },
        'regexes': [
            r"/reports/7/output/\?supply_id=1", ],
        'status_code': 303, },
    {
        'path': '/chellow/reports/305/output/?supply_id=1',
        'regexes': [
            r'value="Hello">',
            r'option value="1" selected>chp</option>', ],
        'status_code': 200, },
    {
        'path': '/chellow/reports/305/output/',
        'method': 'post',

        # Change it back.
        'data': {
            'supply_id': "1",
            'name': "1",
            'source_id': "1",
            'generator_type_id': "1",
            'gsp_group_id': "11", },
        'status_code': 303, },

    # Can we see a supply era ok?
    {
        'name': "view era in edit mode. Supply 1",
        'path': '/chellow/reports/307/output/?era_id=1',

        # Check start date year is there
        'regexes': [
            r"start_year",
            r'<option value="53" selected>HH contract</option>',
            r'"imp_supplier_contract_id">\s*'
            '<option value="55" selected>Half-hourlies 2007',

            # Can we see the MOP account?
            r'"mc-22 9205 6799 106"', ],
        'status_code': 200, },

    # Supply 2
    {
        'path': '/chellow/reports/307/output/?era_id=2',

        # Check site code is correct
        'regexes': [
            r"<td>\s*CI004\s*</td>", ],
        'status_code': 200, },

    # Can we add a new era ok? },
    {
        'name': "Manipulating eras",
        'path': '/chellow/reports/305/output/',
        'method': 'post',
        'data': {
            'supply_id': "2",
            'start_year': "2006",
            'start_month': "07",
            'start_day': "20",
            'start_hour': "00",
            'start_minute': "00",
            'insert_era': "Insert", },
        'regexes': [
            r"/chellow/reports/7/output/\?supply_id=2", ],
        'status_code': 303, },

    # Let's check it's carried forward the import mpan. Supply 2
    {
        'path': '/chellow/reports/307/output/?era_id=8',
        'regexes': [
            r"22 9813 2107 763",
            r'name="mtc_code" value="845" size="3" maxlength="3"', ],
        'status_code': 200, },

    # Can we delete the era ok? Supply 2
    {
        'path': '/chellow/reports/307/output/?era_id=8&delete=Delete',
        'regexes': [
            r"Are you sure you want to delete this", ],
        'status_code': 200, },

    # When a supply era is ended, check that the snags are updated. Supply 5
    {
        'path': '/chellow/reports/307/output/',
        'method': 'post',
        'data': {
            'era_id': "5",
            'start_year': "2003",
            'start_month': "08",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00",
            'is_ended': "true",
            'finish_year': "2003",
            'finish_month': "08",
            'finish_day': "13",
            'finish_hour': "23",
            'finish_minute': "30",
            'gsp_group_id': "11",
            'mop_contract_id': "57",
            'mop_account': "22 0883 6932 301",
            'hhdc_contract_id': "53",
            'hhdc_account': "22 0883 6932 301",
            'msn': "",
            'pc_id': "9",
            'mtc_code': "845",
            'cop_id': "5",
            'ssc_code': "",
            'imp_llfc_code': "570",
            'imp_mpan_core': "22 0883 6932 301",
            'imp_sc': "350",
            'imp_supplier_contract_id': "55",
            'imp_supplier_account': "4341", },
        'status_code': 303, },

    # Check it's correct in edit view
    {
        'path': '/chellow/reports/307/output/?era_id=5',

        # Check start day is correct
        'regexes': [
            r'option value="3" selected>03</option>',

            # Check the end date is right
            r'<input type="checkbox" name="is_ended" value="true" checked',
            r'option value="13" selected>13</option>',
            r'option value="23" selected>23</option>', ],
        'status_code': 200, },

    # Check it's correct in supply view
    {
        'path': '/chellow/reports/7/output/?supply_id=5',
        'status_code': 200,

        # Check the end date is right
        'regexes': [
            r'<a title="2003-08-13 23:30">2003-08-13</a>',
            r'<legend>TRIAD</legend>\s*<input type="hidden" name="supply_id"',
            r'<a href="/chellow/reports/15/output/\?supply_id=5&amp;'
            'is_import=true&amp;year=\d{4}&amp;years=1">Import</a>', ], },

    # Supply 5, Era 5
    {
        'path': '/chellow/reports/301/output/?channel_id=18',
        'status_code': 200,

        # Check the end date is right
        'regexes': [
            r"Channel Export\s*REACTIVE_EXP",
            r"<td>2003-08-03 00:00</td>\s*<td>2003-08-13 23:30</td>\s*"
            "<td>Missing</td>", ], },

    # Check that if the hhdc contract is changed, the hhdc contract of the
    # snags change

    # Check the export supply capacity can be updated as well. Supply 5
    {
        'path': '/chellow/reports/307/output/',
        'method': 'post',
        'data': {
            'era_id': "5",
            'msn': "",
            'start_year': "2003",
            'start_month': "08",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00",
            'is_ended': "true",
            'finish_year': "2003",
            'finish_month': "08",
            'finish_day': "13",
            'finish_hour': "23",
            'finish_minute': "30",
            'mop_contract_id': "57",
            'mop_account': "22 0883 6932 301",
            'hhdc_contract_id': "53",
            'hhdc_account': "22 0883 6932 301",
            'pc_id': "9",
            'mtc_code': "845",
            'cop_id': "5",
            'ssc_code': "",
            'imp_llfc_code': "570",
            'imp_mpan_core': "22 0883 6932 301",
            'imp_gsp_group_id': "11",
            'imp_sc': "430",
            'imp_supplier_contract_id': "55",
            'imp_supplier_account': "4341", },
        'status_code': 303, },

    # Check the change is there in edit view
    {
        'path': '/chellow/reports/307/output/?era_id=5',
        'regexes': [
            r'<input name="imp_sc" value="430" size="9" maxlength="9">', ], },
    {
        'path': '/chellow/reports/301/output/?channel_id=18',
        'status_code': 200,
        'regexes': [
            r"Channel Export\s*REACTIVE_EXP",

            # Check the snag is there
            r"<td>2003-08-03 00:00</td>\s*<td>2003-08-13 23:30</td>\s*"
            "<td>Missing</td>", ], },

    # Put it back to how it was. Supply 5
    {
        'path': '/chellow/reports/307/output/',
        'method': 'post',
        'data': {
            'era_id': "5",
            'msn': "",
            'start_year': "2003",
            'start_month': "08",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00",
            'is_ended': "false",
            'mop_contract_id': "57",
            'mop_account': "22 0883 6932 301",
            'hhdc_contract_id': "53",
            'hhdc_account': "22 0883 6932 301",
            'pc_id': "9",
            'mtc_code': "845",
            'cop_id': "5",
            'ssc_code': "",
            'imp_llfc_code': "570",
            'imp_mpan_core': "22 0883 6932 301",
            'imp_sc': "350",
            'imp_supplier_contract_id': "55",
            'imp_supplier_account': "4341", },
        'status_code': 303, },

    # Valid bulk update of supply eras
    {
        'path': '/chellow/reports/293/output/',
        'method': 'post',
        'files': {'import_file': 'era-update.csv'},
        'status_code': 303,
        'regexes': [
            r"/chellow/reports/295/output/\?process_id=8", ], },
    {
        'path': '/chellow/reports/295/output/?process_id=8',
        'tries': {'max': 10, 'period': 1},

        # Check it's loaded ok
        'regexes': [
            r"The file has been imported successfully", ],
        'status_code': 200, },
    {
        'path': '/chellow/reports/293/output/',
        'method': 'post',
        'files': {'import_file': 'supplies-bad-mpan.csv'},
        'status_code': 303,
        'regexes': [
            r"/reports/295/output/\?process_id=9", ], },
    {
        'path': '/chellow/reports/295/output/?process_id=9',
        'tries': {'max': 10, 'period': 1},

        # Check it's loaded ok
        'regexes': [
            r"The MPAN core 22 9813 2107 763 is already attached to another "
            "supply\.", ],
        'status_code': 200, },

    # Attach another site to an era. Supply 2
    {
        'path': '/chellow/reports/307/output/',
        'method': 'post',
        'data': {
            'era_id': "2",
            'site_code': "CI005",
            'attach': "Attach", },
        'status_code': 303, },

    # Check that we prevent mpan cores from changing without an overlapping
    # period. Supply 2
    {
        'path': '/chellow/reports/307/output/',
        'method': 'post',
        'data': {
            'era_id': "8",
            'msn': "",
            'start_year': "2006",
            'start_month': "07",
            'start_day': "20",
            'start_hour': "00",
            'start_minute': "00",
            'is_ended': "false",
            'mop_contract_id': "57",
            'mop_account': "mc-22 9813 2107 763",
            'hhdc_contract_id': "53",
            'hhdc_account': "01",
            'pc_id': "9",
            'mtc_code': "845",
            'cop_id': "3",
            'ssc_code': "",
            'imp_llfc_code': "570",
            'imp_mpan_core': "2276930477695",
            'imp_sc': "430",
            'imp_supplier_contract_id': "55",
            'imp_supplier_account': "01", },
        'status_code': 400,

        # Also, we've changed the CoP to be 3. Check that this is remembered
        # when there is an error.
        'regexes': [
            r'<option value="3" selected>3 CoP 3</option>',
            r"MPAN cores can&#39;t change without an overlapping period", ], },

    # Check that we get a good error message if the LLFC is of the wrong
    # polarity. Supply 2
    {
        'path': '/chellow/reports/307/output/',
        'method': 'post',
        'data': {
            'era_id': "8",
            'msn': "",
            'start_year': "2006",
            'start_month': "07",
            'start_day': "20",
            'start_hour': "00",
            'start_minute': "00",
            'is_ended': "false",
            'mop_contract_id': "57",
            'mop_account': "mc-22 9813 2107 763",
            'hhdc_contract_id': "53",
            'hhdc_account': "01",
            'pc_id': "9",
            'mtc_code': "845",
            'cop_id': "3",
            'ssc_code': "",
            'imp_llfc_code': "521",
            'imp_mpan_core': "22 9813 2107 763",
            'imp_sc': "430",
            'imp_supplier_contract_id': "55",
            'imp_supplier_account': "01", },
        'status_code': 400,
        'regexes': [
            r"The imp line loss factor 521 is actually an exp one\.", ], },

    # Check it gives a sensible error message if the files doesn't start
    # with #F2
    {
        'name': "Import hh data",
        'path': '/chellow/reports/211/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "53", },
        'files': {'import_file': 'no_hash.df2'},
        'regexes': [
            r"/reports/65/output/\?hhdc_contract_id=53&process_id=0", ],
        'status_code': 303, },
    {
        'path': '/chellow/reports/65/output/?hhdc_contract_id=53&process_id=0',
        'method': 'post',
        'tries': {},
        'regexes': [
            r"The first line must be &#39;#F2&#39;", ],
        'status_code': 200, },

    # Import some hh Stark DF2 data
    {
        'path': '/chellow/reports/211/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "53", },
        'files': {'import_file': 'ftp/hh_data.df2'},
        'status_code': 303,
        'regexes': [
            r"/reports/65/output/\?hhdc_contract_id=53&process_id=1", ], },
    {
        'path': '/chellow/reports/65/output/?hhdc_contract_id=53&process_id=1',
        'tries': {'max': 10, 'period': 1},

        # Check it's loaded ok and has ignored the blank line and the #F2 line
        'regexes': [
            r"The import has completed.*successfully.",

            # Check link to hhdc is correct
            r"/chellow/reports/115/output/\?hhdc_contract_id=53", ],
        'status_code': 200, },

    # Supply 1, era 1
    {
        'path': '/chellow/reports/301/output/?channel_id=4',
        'regexes': [
            r"Channel Export\s*REACTIVE_EXP",
            r'<tr>\s*<td>\s*'
            '<a href="/chellow/reports/117/output/\?snag_id=4">view</a>\s*'
            '</td>\s*<td>2003-08-03 00:00</td>\s*<td>Ongoing</td>\s*'
            '<td>Missing</td>', ],
        'status_code': 200, },

    # Check if more hh data imports ok
    {
        'path': '/chellow/reports/211/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "53", },
        'files': {'import_file': 'hh_data2.df2'},
        'status_code': 303, },

    # This relies on the datum 15/11/2005,00:30,1.0,A being already loaded,
    # with a gap before it.
    {
        'name': "Detect if hh import still works if first hh datum is "
        "missing.",
        'path': '/chellow/reports/211/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "53", },
        'files': {'import_file': 'missing.df2'},
        'regexes': [
            r"/reports/65/output/\?hhdc_contract_id=53&process_id=3", ],
        'status_code': 303, },
    {
        'path': '/chellow/reports/65/output/?hhdc_contract_id=53&process_id=3',
        'tries': {'max': 10, 'period': 1},
        'regexes': [
            r"The import has completed.*successfully.", ],
        'status_code': 200, },

    # This relies on the default timezone being BST },
    {
        'name': "Do we handle BST ok?",
        'path': '/chellow/reports/211/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "53", },
        'files': {'import_file': 'hh_data_timezone.df2'},
        'regexes': [
            r"/chellow/reports/65/output/\?hhdc_contract_id=53&process_id=4",
        ],
        'status_code': 303, },
    {
        'path': '/chellow/reports/65/output/?hhdc_contract_id=53&process_id=4',

        # Check it's loaded ok
        'tries': {'max': 10, 'period': 1},
        'regexes': [
            r"The import has completed.*successfully.", ],
        'status_code': 200, },

    # Test that 3 non-actual reads in a row generate a single snag },
    {
        'name': "Actual reads snags combined properly",
        'path': '/chellow/reports/211/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "53", },
        'files': {'import_file': 'hh_data_not_actual.df2'},
        'regexes': [
            r"/chellow/reports/65/output/\?hhdc_contract_id=53&process_id=5",
            ],
        'status_code': 303, },
    {
        'path': '/chellow/reports/65/output/?hhdc_contract_id=53&process_id=5',
        'tries': {'max': 10, 'period': 1},
        'regexes': [
            r"The import has completed.*successfully.", ],
        'status_code': 200, },

    # supply 1, era 1
    {
        'path': '/chellow/reports/301/output/?channel_id=3',
        'regexes': [
            r"Channel Export\s*ACTIVE",
            r'<td>\s*'
            '<a href="/chellow/reports/117/output/\?snag_id=45">view</a>\s*'
            '</td>\s*<td>2005-12-15 07:00</td>\s*<td>2005-12-15 08:00</td>\s*'
            '<td>Estimated</td>',
            r'<tr>\s*<td>\s*'
            '<a href="/chellow/reports/117/output/\?snag_id=3">view</a>\s*'
            '</td>\s*<td>2003-08-03 00:00</td>\s*<td>2005-12-15 06:30</td>\s*'
            '<td>Missing</td>', ],
        'status_code': 200, },
    {
        'path': '/chellow/reports/211/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "53", },
        'files': {'import_file': 'hh_data_not_actual2.df2'},
        'regexes': [
            r'/reports/65/output/\?hhdc_contract_id=53&process_id=6'],
        'status_code': 303, },
    {
        'path': '/chellow/reports/65/output/?hhdc_contract_id=53&process_id=6',
        'tries': {'max': 10, 'period': 1},
        'regexes': [
            r"The import has completed.*successfully.", ],
        'status_code': 200, },

    # supply 1, era 1
    {
        'path': '/chellow/reports/301/output/?channel_id=3',
        'regexes': [
            r"Channel Export\s*ACTIVE",
            r'<td>\s*'
            '<a href="/chellow/reports/117/output/\?snag_id=45">view</a>\s*'
            '</td>\s*<td>2005-12-15 07:00</td>\s*<td>2005-12-15 09:30</td>\s*'
            '<td>Estimated</td>', ],
        'status_code': 200, },

    # Test if a CSV HH file can be imported },
    {
        'name': "Importing simple CSV data",
        'path': '/chellow/reports/211/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "53", },
        'files': {'import_file': 'hh_data.simple.csv'},
        'regexes': [
            r"/reports/65/output/\?hhdc_contract_id=53&process_id=7", ],
        'status_code': 303, },
    {
        'path': '/chellow/reports/65/output/?hhdc_contract_id=53&process_id=7',
        'tries': {'max': 10, 'period': 1},
        'regexes': [
            r"The import has completed.*successfully.", ],
        'status_code': 200, },

    # Check that the imported HH datum is correct for supply 1, era 1
    {
        'path': '/chellow/reports/301/output/?channel_id=3&start_year=2005&'
        'start_month=09',
        'regexes': [
            r"<td>2005-09-15 00:00</td>\s*<td>1.0</td>\s*<td>A</td>", ], },

    # Check it gives a sensible error message if the comma after the value is
    # missing
    {
        'name': "Various DF2 tests.",
        'path': '/chellow/reports/211/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "53", },
        'files': {'import_file': 'hh_data_malformed.df2'},
        'regexes': [
            r"/reports/65/output/\?hhdc_contract_id=53&process_id=8", ],
        'status_code': 303, },
    {
        'path': '/chellow/reports/65/output/?hhdc_contract_id=53&process_id=8',
        'tries': {'max': 10, 'period': 1},
        'regexes': [
            r"Problem at line number: 4", ],
        'status_code': 200, },

    # Check it gives a sensible error message if the first mpan is malformed
    {
        'path': '/chellow/reports/211/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "53", },
        'files': {'import_file': 'hh_data_bad_beginning.df2'},
        'regexes': [
            r"/reports/65/output/\?hhdc_contract_id=53&process_id=9", ],
        'status_code': 303, },
    {
        'path': '/chellow/reports/65/output/?hhdc_contract_id=53&process_id=9',
        'tries': {'max': 10, 'period': 1},
        'regexes': [
            r"The MPAN core &#39;2204707514535,,,&#39; must contain exactly "
            "13 digits", ],
        'status_code': 200, },

    # Check sensible error message if header but no data
    {
        'path': '/chellow/reports/211/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "53", },
        'files': {'import_file': 'hh_data_header_but_no_data.df2'},
        'regexes': [
            r"/reports/65/output/\?hhdc_contract_id=53&process_id=10", ],
        'status_code': 303, },
    {
        'path': '/chellow/reports/65/output/?hhdc_contract_id=53&'
        'process_id=10',
        'tries': {'max': 10, 'period': 1},
        'regexes': [
            r"The import has completed.*successfully\.", ],
        'status_code': 200, },

    # Make sure 'show HH data' button works, supply 6, era 6 },
    {
        'name': "Manipulate channels",
        'path': '/chellow/reports/301/output/?channel_id=19',
        'regexes': [
            r"Import\s*ACTIVE", ],
        'status_code': 200, },

    # Manipulate Hh data"
    {
        'name': "Make sure 'show HH data' button works, supply 6, era 6",
        'path': '/chellow/reports/301/output/?channel_id=21',
        'regexes': [
            r"Export\s*REACTIVE_EXP",
            r'action="\.">', ],
        'status_code': 200, },
    {
        'name': "Give good error for invalid date.",
        'path': '/chellow/reports/301/output/?channel_id=21&start_year=2006&'
        'start_month=13',
        'regexes': [
            r"Invalid date", ],
        'status_code': 400, },
    {
        'name': "Check site level snag",
        'path': '/chellow/reports/39/output/',
        'regexes': [
            r"CI004",

            # There's an hh where export to net is *less* than imported from
            # generator, check this doesn't show up.
            r'<td>\s*'
            '<a href="/chellow/reports/119/output/\?site_snag_id=43">view</a> '
            '\[<a href="/chellow/reports/373/'
            'output/\?site_snag_id=43">edit</a>\]\s*</td>\s*<td>[^<]*</td>\s*'
            '<td>\s*'
            '<a href="/chellow/reports/5/output/\?site_id=1">CI004</a>\s*'
            '</td>\s*<td>Lower Treave</td>\s*'
            '<td>Export to net &gt; import from generators.</td>\s*'
            '<td>2005-10-29 23:30</td>\s*<td>\s*2005-10-30 01:00</td>\s*'
            '</tr>\s*</tbody>', ],
        'status_code': 200, },
    {
        'path': '/chellow/reports/371/output/',

        # Check that there's an 'ignore-year' parameter.
        'regexes': [
            r'name="ignore_year"', ],
        'status_code': 200, },

    # Supply 1, era 1 },
    {
        'name': "Check view of channel level snag",
        'path': '/chellow/reports/117/output/?snag_id=1',
        'status_code': 200, },

    # Check that for a supply with multiple eras, a channel without any data
    # can be deleted. This test needs some hh data loaded somewhere. Supply 2,
    # era 8, exp active
    {
        'name': "Delete channel without data",
        'path': '/chellow/reports/303/output/',
        'method': 'post',
        'data': {
            'channel_id': "25",
            'delete': "Delete", },
        'status_code': 303, },

    # Put it back to how it was before. Supply 2
    {
        'path': '/chellow/reports/299/output/',
        'method': 'post',
        'data': {
            'era_id': "8",
            'imp_related': "false",
            'channel_type': "ACTIVE", },
        'status_code': 303, },

    # Check it gives an error if the hhdc contract is removed from a supply era
    # that has data. Supply 1
    {
        'path': '/chellow/reports/307/output/',
        'method': 'post',
        'data': {
            'era_id': "1",
            'start_year': "2003",
            'start_month': "08",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00",
            'is_ended': "false",
            'msn': "",
            'gsp_group_id': "11",
            'pc_id': "9",
            'hhdc_contract_id': "null",
            'hhdc_account': "01",
            'imp_mtc_code': "845",
            'imp_llfc_code': "550",
            'imp_mpan_core': "22 9205 6799 106",
            'imp_ssc_code': "",
            'imp_sc': "450",
            'imp_supplier_contract_id': "6",
            'imp_supplier_account': "11640077",
            'exp_mtc_code': "845",
            'exp_llfc_code': "581",
            'exp_mpan_core': "22 0470 7514 535",
            'exp_ssc_code': "",
            'exp_sc': "150",
            'exp_supplier_contract_id': "6",
            'exp_supplier_account': "01", },
        'status_code': 400, },
    {
        'name': "View a snag",
        'path': '/chellow/reports/119/output/?site_snag_id=43',
        'status_code': 200,
        'regexes': [
            r"<th>Finish Date</th>\s*<td>2005-10-30 01:00</td>", ], },

    # Assumes various site snags are present at this stage },
    {
        'name': "site snags stay ignored",
        'path': '/chellow/reports/371/output/',
        'method': 'post',
        'data': {
            'ignore_year': "2006",
            'ignore_month': "12",
            'ignore_day': "26",
            'ignore_hour': "00",
            'ignore_minute': "00",
            'ignore': "Ignore", },
        'status_code': 303, },
    {
        'path': '/chellow/reports/211/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "53", },
        'files': {'import_file': 'ftp/hh_data.df2'},
        'regexes': [
            r"/reports/65/output/\?hhdc_contract_id=53&process_id=11", ],
        'status_code': 303, },
    {
        'path': '/chellow/reports/65/output/?hhdc_contract_id=53&'
        'process_id=11',
        'tries': {'max': 10, 'period': 1},
        'regexes': [
            r"The import has completed.*successfully", ],
        'status_code': 200, },
    {
        'path': '/chellow/reports/39/output/',
        'regexes': [
            r"<tbody>\s*</tbody>", ],
        'status_code': 200, },
    {
        'path': '/chellow/reports/17/output/?supply_id=5&months=1&'
        'finish_year=2010&finish_month=03',
        'regexes': [
            r"<tr>\s*<td>\s*2010-03-15 12:00\s*</td>\s*<td>0</td>\s*"
            "<td>A</td>", ],
        'status_code': 200, },

    # Create a new batch },
    {
        'name': "Batches",
        'path': '/chellow/reports/287/output/',
        'method': 'post',
        'data': {
            'supplier_contract_id': "55",
            'reference': "04-003",
            'description': "Contract 4, batch number 3", },
        'status_code': 303, },

    # Check it gives a good error message for a duplicate name
    {
        'path': '/chellow/reports/287/output/',
        'method': 'post',
        'data': {
            'supplier_contract_id': "55",
            'reference': "04-003",
            'description': "dup batch", },
        'regexes': [
            r"There&#39;s already a batch attached to the contract "
            "Half-hourlies 2007 with the reference 04-003\.", ],
        'status_code': 400, },

    # Create a new import. Supplier contract 55 },
    {
        'name': "Bill imports",
        'path': '/chellow/reports/321/output/',
        'method': 'post',
        'data': {
            'supplier_batch_id': "1", },
        'files': {'import_file': 'bills.mm'},
        'status_code': 303,
        'regexes': [
            r"/reports/323/output/\?importer_id=0", ], },

    # Supplier contract 55, batch 1
    {
        'path': '/chellow/reports/323/output/?importer_id=0',
        'tries': {'max': 10, 'period': 1},
        'status_code': 200,
        'regexes': [
            r"<td>2007-02-28 00:00</td>\s*<td>0</td>\s*<td>4463.08</td>",
            r"All the bills have been successfully loaded and attached to the "
            "batch\.", ], },

    # Valid import of supplies },
    {
        'name': "Set up NHH",
        'path': '/chellow/reports/293/output/',
        'method': 'post',
        'files': {'import_file': 'nhh-supplies.csv'},
        'status_code': 303,
        'regexes': [
            r"/reports/295/output/\?process_id=10", ], },
    {
        'path': '/chellow/reports/295/output/?process_id=10',
        'tries': {'max': 10, 'period': 1},

        # Check it's loaded ok
        'regexes': [
            r"The file has been imported successfully", ],
        'status_code': 200, },

    # Check values have been imported correctly. Supply 11
    {
        'path': '/chellow/reports/307/output/?era_id=11',
        'regexes': [
            r"K87D74429", ],
        'status_code': 200, },

    # Create a new batch
    {
        'path': '/chellow/reports/287/output/',
        'method': 'post',
        'data': {
            'supplier_contract_id': "59",
            'reference': "06-002",
            'description': "Bgb batch", },
        'status_code': 303, },

    # Supplier contract 59
    {
        'path': '/chellow/reports/321/output/',
        'method': 'post',
        'data': {
            'supplier_batch_id': "3", },
        'files': {'import_file': 'bills.bgb.edi'},
        'status_code': 303,
        'regexes': [
            r"/reports/323/output/\?importer_id=1", ], },

    # Supplier contract 59, batch 3
    {
        'path': '/chellow/reports/323/output/?importer_id=1',
        'tries': {'max': 10, 'period': 1},
        'status_code': 200,
        'regexes': [
            r"All the bills have been successfully loaded and attached to the "
            "batch\.", ], },

    # Set a previously estimated HH to actual, supply 1, era 1, channel 3 },
    {
        'name': "Check that resolved HH estimates have their snags cleared.",
        'path': '/chellow/reports/309/output/',
        'method': 'post',
        'data': {
            'update': "Update",
            'hh_datum_id': "12",
            'value': "0.5",
            'status': "A", },
        'status_code': 303, },

    # Check that the snag has been cleared. Supply 1, era 1
    {
        'path': '/chellow/reports/301/output/?channel_id=3',
        'regexes': [
            r"Channel Export\s*ACTIVE",
            r"<td>2005-12-15 07:30</td>\s*<td>2005-12-15 09:30</td>\s*"
            "<td>Estimated</td>", ], },

    # Change it back. supply 1, era 1.
    {
        'path': '/chellow/reports/309/output/',
        'method': 'post',
        'data': {
            'hh_datum_id': "12",
            'value': "0.5",
            'status': "E", },
        'status_code': 303, },
    {
        'name': "Test of BGlobal HH data import",
        'path': '/chellow/reports/211/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "53", },
        'files': {'import_file': 'hh_data.bg.csv'},
        'status_code': 303,
        'regexes': [
            r"/chellow/reports/65/output/\?hhdc_contract_id=53&process_id=12",
        ], },
    {
        'path': '/chellow/reports/65/output/?hhdc_contract_id=53'
        '&process_id=12',
        'tries': {'max': 10, 'period': 1},
        'regexes': [
            r"The import has completed.*successfully.", ],
        'status_code': 200, },

    # supply 1, era 1 },
    {
        'name': "Check the BGlobal data is imported to the right number of "
        "sig figs",
        'path': '/chellow/reports/301/output/?channel_id=1&start_year=2008&'
        'start_month=07',
        'regexes': [
            r"0\.262", ], },
    {
        'name': "Check okay if supply era update is interupted by an error. "
        "Supply 9",
        'path': '/chellow/reports/307/output/',
        'method': 'post',
        'data': {
            'era_id': "9",
            'msn': "P96C93722",
            'start_year': "2005",
            'start_month': "08",
            'start_day': "06",
            'is_ended': "false",
            'pc_id': "9",
            'mtc_code': "535",
            'llfc_code': "510",
            'imp_mpan_core': "22 0195 4836 192",
            'ssc_code': "0127",
            'gsp_group_id': "11",
            'imp_sc': "30",
            'hhdc_contract_id': "HH contract",
            'hhdc_account': "",
            'imp_supplier_contract_id': "Non half-hourlies 2007",
            'imp_supplier_account': "341664",

            # Should error on this
            'exp_mpan_core': "99 0000 4444 883",
            'exp_sc': "200",
            'exp_supplier_contract_id': "Non half-hourlies 2007",
            'exp_supplier_account': "341664", },
        'status_code': 400, },
    {
        'name': "HH data general import",
        'path': '/chellow/reports/293/output/',
        'method': 'post',
        'files': {'import_file': 'hh_data.csv'},
        'status_code': 303,
        'regexes': [
            r"/chellow/reports/295/output/\?process_id=11", ], },
    {
        'path': '/chellow/reports/295/output/?process_id=11',
        'tries': {'max': 10, 'period': 1},
        'regexes': [
            r"The file has been imported successfully\.", ],
        'status_code': 200, },

    # Create new batch },
    {
        'name': "CSV import",
        'path': '/chellow/reports/287/output/',
        'method': 'post',
        'data': {
            'supplier_contract_id': "55",
            'reference': "06-004",
            'description': "CSV batch", },
        'status_code': 303, },

    # Insert bills. Supplier contract 55
    {
        'path': '/chellow/reports/321/output/',
        'method': 'post',
        'data': {
            'supplier_batch_id': "4", },
        'files': {'import_file': 'bills.csv'},
        'status_code': 303,
        'regexes': [
            r"/reports/323/output/\?importer_id=2", ], },

    # Supplier contract 54, batch 4
    {
        'path': '/chellow/reports/323/output/?importer_id=2',
        'tries': {'max': 10, 'period': 1},
        'status_code': 200,
        'regexes': [
            r"All the bills have been successfully loaded and attached to the "
            "batch\.", ], },

    # First create the era },
    {
        'name': "Check one is able to delete an era ok",
        'path': '/chellow/reports/305/output/',
        'method': 'post',
        'data': {
            'supply_id': "9",
            'start_year': "2009",
            'start_month': "01",
            'start_day': "20",
            'start_hour': "00",
            'start_minute': "00",
            'insert_era': "Insert", },
        'regexes': [
            r"/chellow/reports/7/output/\?supply_id=9", ],
        'status_code': 303, },

    # Delete era. Supply 9
    {
        'path': '/chellow/reports/307/output/',
        'method': 'post',
        'data': {
            'era_id': "12",
            'delete': "Delete", },
        'status_code': 303, },
    {
        'name': "Check 'view' link is correct on a site in the edit world.",
        'path': '/chellow/reports/311/output/?site_id=7',
        'regexes': [
            r"/chellow/reports/5/output/\?site_id=7", ],
        'status_code': 200, },
    {
        'name': "Check that if era dates change, hh data move with them.",
        'path': '/chellow/reports/305/output/',
        'method': 'post',
        'data': {
            'supply_id': "1",
            'start_year': "2008",
            'start_month': "7",
            'start_day': "7",
            'start_hour': "00",
            'start_minute': "00",
            'insert_era': "Insert", },
        'regexes': [
            r"/chellow/reports/7/output/\?supply_id=1", ],
        'status_code': 303, },

    # supply 1, era 13
    {
        'path': '/chellow/reports/301/output/?channel_id=32&start_year=2008&'
        'start_month=07',
        'regexes': [
            r'<td>\s*'
            '\[<a href="/chellow/reports/309/output/\?hh_datum_id=66">'
            'edit</a>\]\s*</td>\s*<td>2008-07-07 00:00</td>\s*'
            '<td>0.247</td>\s*<td>A</td>', ],
        'status_code': 200, },
    {
        'name': "Check 'view' link is correct on a supply in the edit world.",
        'path': '/chellow/reports/305/output/?supply_id=10',
        'regexes': [
            r"/chellow/reports/7/output/\?supply_id=10", ],
        'status_code': 200, },
    {
        'name': "Check site nav link is correct on site HH data page.",
        'path': '/chellow/reports/25/output/?site_code=CI004&year=2005&'
        'month=11',
        'regexes': [
            r"/chellow/reports/5/output/\?site_id=1",

            # Check that columns are in the right order
            r'kWh</th>\s*<th colspan="4">\s*1 net\s*</th>', ],
        'status_code': 200, },
    {
        'name': "Check no duplicate supplies in Supplies Duration report.",
        'path': '/chellow/reports/149/output/?start_year=2008&start_month=07&'
        'start_day=01&start_hour=0&start_minute=0&finish_year=2008&'
        'finish_month=07&finish_day=31&finish_hour=23&finish_minute=30',
        'regexes': [
            # Check starts with titles
            r'\)\s\sSupply',

            r'("1","1","net","","CH017",){1}',

            # Check full line
            r'"2","1","net","","CI004","Lower Treave","2008-07-01 00:00",'
            '"2008-07-31 23:30","00","845","5","","0","hh",'
            '570,22 9813 2107 763,430,Half-hourlies 2007,0,0,0.0,0,,None,1488,'
            '581,22 3475 1614 211,900,Half-hourlies 2007,0,0,,0,,None,1488',

            ],
        'status_code': 200, },

    # Delete a day of data. Supply 1, era 13 },
    {
        'name': "Check last HH is deleted when a day of HH data is deleted.",
        'path': '/chellow/reports/303/output/',
        'method': 'post',
        'data': {
            'channel_id': "32",
            'start_year': "2008",
            'start_month': "07",
            'start_day': "07",
            'start_hour': "00",
            'start_minute': "00",
            'finish_year': "2008",
            'finish_month': "07",
            'finish_day': "07",
            'finish_hour': "23",
            'finish_minute': "30",
            'delete_data': "Delete", },
        'regexes': [
            r"Data successfully deleted\.", ],
        'status_code': 200, },

    # Check the last HH of the day is deleted. Supply 1, era 13
    {
        'path': '/chellow/reports/301/output/?channel_id=32&start_year=2008&'
        'start_month=07',
        'regexes': [
            r'<tbody>\s*<tr>\s*<td>\s*'
            '\[<a href="/chellow/reports/309/output/\?hh_datum_id=114">'
            'edit</a>\]\s*</td>\s*<td>2008-07-08 00:00</td>\s*'
            '<td>0.299</td>\s*<td>A</td>', ],
        'status_code': 200, },

    # supply 1, era 1, channel 1 },
    {
        'name': "Check one is redirected to hh data when a datum is deleted.",
        'path': '/chellow/reports/309/output/?hh_datum_id=23',
        'method': 'post',
        'data': {
            'delete': "Delete", },
        'status_code': 303,
        'regexes': [
            r"/chellow/reports/301/output/\?channel_id=1", ], },

    # Supply 5 },
    {
        'name': "Test that it gives an error if the hhdc_contract_id is null.",
        'path': '/chellow/reports/307/output/',
        'method': 'post',
        'data': {
            'era_id': "5",
            'msn': "",
            'start_year': "2003",
            'start_month': "08",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00",
            'is_ended': "false",
            'mop_contract_id': "57",
            'mop_account': "22 0883 6932 301",
            'hhdc_contract_id': "null",
            'pc_id': "9",
            'mtc_code': "845",
            'cop_id': "5",
            'ssc_code': "",
            'imp_llfc_code': "570",
            'imp_mpan_core': "22 0883 6932 301",
            'imp_sc': "350",
            'imp_supplier_contract_id': "55",
            'imp_supplier_account': "01", },
        'status_code': 400,
        'regexes': [
            r"Problem parsing the field hhdc_contract_id as an integer: "
            "invalid literal for int\(\) with base 10: .*null", ], },
    {
        'name': "Test that profile 05 is displayed for an era. Supply 9",
        'path': '/chellow/reports/307/output/?era_id=9',
        'regexes': [
            r'<option value="5" selected>05 - Non-domestic, MD, load factor '
            '0-20%</option>', ],
        'status_code': 200, },
    {
        'name': "Try adding a party viewer.",
        'path': '/chellow/reports/255/output/',
        'method': 'post',
        'data': {
            'email_address': "mishka@localhost",
            'password': "fyodor",
            'user_role_code': "party-viewer",
            'party_id': "97", },  # DASL HHDC

        'status_code': 303,
        'regexes': [
            r"/chellow/reports/257/output/\?user_id=5", ], },
    {
        'name': "Check that the party viewer is able to view snags.",
        'path': '/chellow/reports/37/output/?'
        'hhdc-contract-id=53&hidden_days=5',
        'auth': ('mishka@localhost', 'fyodor'),
        'regexes': [
            r"<td>\s*22 0470 7514 535\s*</td>\s*<td>\s*<ul>\s*<li>\s*"
            "CH017 Parbola\s*</li>",
            r"There are 46 snag\(s\) older than 5 days that aren't ignored\.",
            r'<a href="/chellow/reports/115/output/\?hhdc_contract_id=53">HH '
            'contract</a>',
            r'<li>\s*'
            '<a href="/chellow/reports/117/output/\?snag_id=1">view</a>  '
            '\[<a href="/chellow/reports/365/output/\?snag_id=1">edit</a>\]\s*'
            '</li>', ],
        'status_code': 200, },
    {
        'name': "Make sure everything's there on the home page.",
        'path': '/chellow/reports/1/output/',
        'auth': ('watkins@example.com', 'alan'),
        'regexes': [
            r'<a href="/chellow/reports/133/output/">Meter Payment Types</a>',
            r'<a href="/chellow/reports/337/output/">\s*Sources\s*</a>',
            r'<a href="/chellow/reports/341/output/">\s*Generator Types\s*'
            '</a>', ],
        'status_code': 200, },

    # Supplier contract 58 },
    {
        'name': "Test deleting the only rate script attached to a supplier "
        "contract.",
        'path': '/chellow/reports/319/output/',
        'method': 'post',
        'data': {
            'supplier_rate_script_id': "307",
            'delete': "Delete", },
        'regexes': [
            r"You can&#39;t delete the last rate script\.", ],
        'status_code': 400, },
    {
        'name': "Try adding a second rate script (set to 'ongoing'), and see "
        "if the era can be updated.",
        'path': '/chellow/reports/325/output/',
        'method': 'post',
        'data': {
            'supplier_contract_id': "59",
            'start_year': "2009",
            'start_month': "08",
            'start_day': "16",
            'start_hour': "00",
            'start_minute': "00",
            'script': "", },
        'status_code': 303, },

    # Supply 1
    {
        'path': '/chellow/reports/307/output/',
        'method': 'post',
        'data': {
            'era_id': "13",
            'start_year': "2008",
            'start_month': "07",
            'start_day': "07",
            'start_hour': "00",
            'start_minute': "00",
            'is_ended': "false",
            'mop_contract_id': "57",
            'mop_account': "mc-22 0470 7514 535",
            'hhdc_contract_id': "53",
            'hhdc_account': "01",
            'msn': "",
            'pc_id': "9",
            'mtc_code': "845",
            'cop_id': "5",
            'ssc_code': "",
            'exp_llfc_code': "581",
            'exp_mpan_core': "22 0470 7514 535",
            'exp_sc': "150",
            'exp_supplier_contract_id': "59",
            'exp_supplier_account': "010", },
        'status_code': 303, },
    {
        'name': "Check updating of HHDC contract state.",
        'path': '/chellow/reports/279/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "53",
            'state': """{
'last_import_keys': {'.': '1960-11-30 00:00_example.csv'}}
""",
            'update_state': "Update State", },
        'status_code': 303, },
    {
        'path': '/chellow/reports/115/output/?hhdc_contract_id=53',
        'status_code': 200,
        'regexes': [
            r"\{\s*&#39;last_import_keys&#39;: \{&#39;.&#39;: "
            "&#39;1960-11-30 00:00_example.csv&#39;\}\}",

            # Check link to channel snags
            r"hidden_days",

            # Check link to add a rate script
            r'Rate Scripts\s*'
            '\[<a href="/chellow/reports/383/output/\?hhdc_contract_id=53">'
            'add</a>\]', ], },

    # Requires that no other user reports have been created. },
    {
        'name': "Check adding of user report.",
        'path': '/chellow/reports/',
        'method': 'post',
        'data': {
            'is_core': "false",
            'name': "Minority Report", },
        'status_code': 303,
        'regexes': [
            r"/reports/2/", ], },
    {
        'path': '/chellow/reports/2/',
        'status_code': 200,
        'regexes': [
            r"Minority Report", ], },

    # Insert era },
    {
        'name': "Check dates are correct for four eras.",
        'path': '/chellow/reports/305/output/',
        'method': 'post',
        'data': {
            'supply_id': "1",
            'start_year': "2008",
            'start_month': "08",
            'start_day': "07",
            'start_hour': "00",
            'start_minute': "00",
            'insert_era': "insert_era", },
        'status_code': 303, },
    {
        'path': '/chellow/reports/305/output/',
        'method': 'post',
        'data': {
            'supply_id': "1",
            'start_year': "2008",
            'start_month': "09",
            'start_day': "07",
            'start_hour': "00",
            'start_minute': "00",
            'insert_era': "insert_era", },
        'status_code': 303, },
    {
        'path': '/chellow/reports/305/output/?supply_id=1',
        'regexes': [
            r"<tr>\s*<td>2003-08-03 00:00</td>\s*<td>2008-07-06 23:30", ],
        'status_code': 200, },
    {
        'name': "Test 'view' link from supplier contract rate scripts.",
        'path': '/chellow/reports/325/output/?supplier_contract_id=59',
        'regexes': [
            r"/chellow/reports/77/output/\?supplier_contract_id=59", ], },
    {
        'name': "Check 'HH Contract' option is there. Supply 9.",
        'path': '/chellow/reports/307/output/?era_id=9',
        'regexes': [
            r'<option value="53">HH contract</option>\s*</select>', ], },
    {
        'name': "Try bulk delete of HHDC snags.",
        'path': '/chellow/reports/279/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "54",
            'ignore_year': "2010",
            'ignore_month': "01",
            'ignore_day': "13",
            'ignore_hour': "00",
            'ignore_minute': "00",
            'ignore_snags': "", },
        'status_code': 303, },
    {
        'name': "Check python compile error gives a reasonable message.",
        'path': '/chellow/reports/317/output/',
        'method': 'post',
        'data': {
            'supplier_contract_id': "55",
            'party_id': "22",  # BIZZ
            'name': "Half-hourlies 2007",
            'charge_script': """
def virtual_bill(supply, startDate, finishDate, pw):
    syntax error
""",
            'properties': "{}", },
        'regexes': [
            r"<li>invalid syntax \(&lt;unknown&gt;, line 3\)</li>"],
        'status_code': 400, },

    # Put back to how it was before
    {
        'path': '/chellow/reports/317/output/',
        'method': 'post',
        'data': {
            'supplier_contract_id': "55",
            'party_id': "22",
            'name': "Half-hourlies 2007",
            'charge_script': """from net.sf.chellow.monad import Monad
import datetime
import pytz
from dateutil.relativedelta import relativedelta

Monad.getUtils()['impt'](
    globals(), 'db', 'utils', 'templater', 'triad', 'computer', 'ccl', 'bsuos',
    'tlms', 'duos', 'system_price')

HH = utils.HH

def virtual_bill_titles():
    return [
        'net-gbp', 'tlm', 'ccl-kwh', 'ccl-rate', 'ccl-gbp',
        'data-collection-gbp', 'duos-availability-kva',
        'duos-availability-days', 'duos-availability-rate',
        'duos-availability-gbp', 'duos-excess-availability-kva',
        'duos-excess-availability-days', 'duos-excess-availability-rate',
        'duos-excess-availability-gbp','duos-day-kwh', 'duos-day-gbp',
        'duos-night-kwh', 'duos-night-gbp', 'duos-reactive-rate',
        'duos-reactive-gbp', 'duos-standing-gbp', 'settlement-gbp',
        'night-msp-kwh', 'night-gsp-kwh', 'night-gbp', 'other-msp-kwh',
        'other-gsp-kwh', 'other-gbp', 'summer-pk-msp-kwh', 'summer-pk-gsp-kwh',
        'summer-pk-gbp', 'winter-low-pk-msp-kwh', 'winter-low-pk-gsp-kwh',
        'winter-low-pk-gbp', 'winter-off-pk-msp-kwh', 'winter-off-pk-gsp-kwh',
        'winter-off-pk-gbp', 'winter-pk-msp-kwh', 'winter-pk-gsp-kwh',
        'winter-pk-gbp', 'bsuos-kwh', 'bsuos-rate', 'bsuos-gbp',
        'triad-actual-1-date', 'triad-actual-1-msp-kw',
        'triad-actual-1-status', 'triad-actual-1-laf', 'triad-actual-1-gsp-kw',
        'triad-actual-2-date', 'triad-actual-2-msp-kw',
        'triad-actual-2-status', 'triad-actual-2-laf', 'triad-actual-2-gsp-kw',
        'triad-actual-3-date', 'triad-actual-3-msp-kw',
        'triad-actual-3-status', 'triad-actual-3-laf', 'triad-actual-3-gsp-kw',
        'triad-actual-gsp-kw', 'triad-actual-rate', 'triad-actual-gbp',
        'triad-estimate-1-date', 'triad-estimate-1-msp-kw',
        'triad-estimate-1-status', 'triad-estimate-1-laf',
        'triad-estimate-1-gsp-kw', 'triad-estimate-2-date',
        'triad-estimate-2-msp-kw', 'triad-estimate-2-status',
        'triad-estimate-2-laf', 'triad-estimate-2-gsp-kw',
        'triad-estimate-3-date', 'triad-estimate-3-msp-kw',
        'triad-estimate-3-status', 'triad-estimate-3-laf',
        'triad-estimate-3-gsp-kw', 'triad-estimate-gsp-kw',
        'triad-estimate-rate', 'triad-estimate-months', 'triad-estimate-gbp',
        'triad-all-estimates-months', 'triad-all-estimates-gbp', 'problem']

def displaced_virtual_bill_titles():
    return [
        'net-gbp', 'bsuos-kwh', 'bsuos-rate', 'bsuos-gbp', 'ccl-kwh',
        'ccl-rate', 'ccl-gbp', 'ssp-rate', 'tlm', 'duos-green-kwh',
        'duos-green-rate', 'duos-green-gbp', 'duos-reactive-gbp',
        'duos-reactive-working', 'duos-standing-gbp', 'night-gbp',
        'night-gsp-kwh', 'night-msp-kwh', 'other-gbp', 'other-gsp-kwh',
        'other-msp-kwh', 'summer-pk-gbp', 'summer-pk-gsp-kwh',
        'summer-pk-msp-kwh', 'triad-gbp', 'triad-working', 'winter-low-pk-gbp',
        'winter-low-pk-gsp-kwh', 'winter-low-pk-msp-kwh', 'winter-off-pk-gbp',
        'winter-off-pk-gsp-kwh', 'winter-off-pk-msp-kwh', 'winter-pk-gbp',
        'winter-pk-gsp-kwh', 'winter-pk-msp-kwh', 'triad-actual-1-date',
        'triad-actual-1-msp-kw', 'triad-actual-1-status', 'triad-actual-1-laf',
        'triad-actual-1-gsp-kw', 'triad-actual-2-date',
        'triad-actual-2-msp-kw', 'triad-actual-2-status', 'triad-actual-2-laf',
        'triad-actual-2-gsp-kw', 'triad-actual-3-date',
        'triad-actual-3-msp-kw', 'triad-actual-3-status', 'triad-actual-3-laf',
        'triad-actual-3-gsp-kw', 'triad-actual-gsp-kw', 'triad-actual-rate',
        'triad-actual-gbp', 'triad-estimate-1-date', 'triad-estimate-1-msp-kw',
        'triad-estimate-1-status', 'triad-estimate-1-laf',
        'triad-estimate-1-gsp-kw', 'triad-estimate-2-date',
        'triad-estimate-2-msp-kw', 'triad-estimate-2-status',
        'triad-estimate-2-laf', 'triad-estimate-2-gsp-kw',
        'triad-estimate-3-date', 'triad-estimate-3-msp-kw',
        'triad-estimate-3-status', 'triad-estimate-3-laf',
        'triad-estimate-3-gsp-kw', 'triad-estimate-gsp-kw',
        'triad-estimate-rate', 'triad-estimate-months', 'triad-estimate-gbp',
        'triad-all-estimates-months', 'triad-all-estimates-gbp', 'problem']

slot_names = [
    'winter-pk', 'winter-low-pk', 'winter-off-pk', 'summer-pk', 'night',
    'other']

slots = {}
for slot_name in slot_names:
    slots[slot_name] = {
        'msp-kwh': slot_name + '-msp-kwh', 'gsp-kwh': slot_name + '-gsp-kwh',
        'gbp': slot_name + '-gbp'}


def displaced_virtual_bill(supply_source):
    bill = supply_source.supplier_bill

    # just check that revolving works
    supply_source.revolve_to_3rd_party_used()
    supply_source.revolve_to_gen_used()

    for slot_name in slot_names:
        slot_keys = slots[slot_name]
        bill[slot_keys['msp-kwh']] = 0
        bill[slot_keys['gsp-kwh']] = 0


    supply_source.is_green = False
    duos.duos_vb(supply_source)

    for hh in supply_source.hh_data:
        is_weekday = hh['utc-day-of-week'] < 5
        if is_weekday and hh['utc-month'] in (1, 12) and \
                16 < hh['utc-decimal-hour'] <= 19:
            slot_key = 'winter-pk'
        elif is_weekday and hh['utc-month'] in (2, 11) and \
                16 < hh['utc-decimal-hour'] <= 19:
            slot_key = 'winter-low-pk'
        elif is_weekday and (hh['utc-month'] > 10 or hh['utc-month'] < 4) and \
                8 < hh['utc-decimal-hour'] <= 20:
            slot_key = 'winter-off-pk'
        elif is_weekday and (hh['utc-month'] > 3 or hh['utc-month'] < 11) and \
                8 < hh['utc-decimal-hour'] <= 20:
            slot_key = 'summer-pk'
        elif 0 < hh['utc-decimal-hour'] <= 7:
            slot_key = 'night'
        else:
            slot_key = 'other'
        slot_keys = slots[slot_key]
        bill[slot_keys['msp-kwh']] += hh['msp-kwh']
        bill[slot_keys['gsp-kwh']] += hh['gsp-kwh']
        rates = supply_source.hh_rate(
            db_id, hh['start-date'], 'gsp_gbp_per_kwh')
        bill[slot_keys['gbp']] += hh['gsp-kwh'] * rates[slot_name]

    ccl.ccl(supply_source)

    for suffix in ['kwh', 'rate', 'gbp']:
        key = 'lec-' + suffix
        if key in bill:
            del bill[key]

    triad.triad_bill(supply_source)
    tlms.hh(supply_source)
    bsuos.hh(supply_source)
    system_price.hh(supply_source)

    for rate_name, rate_set in supply_source.supplier_rate_sets.iteritems():
        if len(rate_set) == 1:
            bill[rate_name] = rate_set.pop()

    for k in bill.keys():
        if k.startswith('duos-reactive-'):
            del bill[k]

    bill['net-gbp'] = sum(v for k, v in bill.iteritems() if k[-4:] == '-gbp')


def virtual_bill(supply_source):
    duos.duos_vb(supply_source)
    bill = supply_source.supplier_bill
    bill.update(
        {
            'net-gbp': 0, 'data-collection-gbp': 0, 'settlement-gbp': 0,
            'problem': ''})

    for slot_name in slot_names:
        slot_keys = slots[slot_name]
        bill[slot_keys['msp-kwh']] = 0
        bill[slot_keys['gsp-kwh']] = 0


    llfc_code = supply_source.llfc_code
    voltage_level = supply_source.voltage_level_code
    is_substation = supply_source.is_substation
    supply_capacity = supply_source.sc
    supply_source.is_green = False

    for datum in supply_source.hh_data:
        is_weekday = datum['utc-day-of-week'] < 5
        if is_weekday and datum['utc-month'] in (1, 12) and \
                16 < datum['utc-decimal-hour'] <= 19:
            slot_key = 'winter-pk'
        elif is_weekday and datum['utc-month'] in (2, 11) and \
                16 < datum['utc-decimal-hour'] <= 19:
            slot_key = 'winter-low-pk'
        elif is_weekday and \
                (datum['utc-month'] > 10 or datum['utc-month'] < 4) and \
                8 < datum['utc-decimal-hour'] <= 20:
            slot_key = 'winter-off-pk'
        elif is_weekday and \
                (datum['utc-month'] > 3 or datum['utc-month'] < 11) and \
                8 < datum['utc-decimal-hour'] <= 20:
            slot_key = 'summer-pk'
        elif 0 < datum['utc-decimal-hour'] <= 7:
            slot_key = 'night'
        else:
            slot_key = 'other'
        slot_keys = slots[slot_key]
        bill[slot_keys['msp-kwh']] += datum['msp-kwh']
        bill[slot_keys['gsp-kwh']] += datum['gsp-kwh']

    month_begin = datetime.datetime(
        supply_source.start_date.year, supply_source.start_date.month, 1,
        tzinfo=pytz.utc)
    month_end = month_begin + relativedelta(months=1) - HH

    ccl.ccl(supply_source)

    for suffix in ['kwh', 'rate', 'gbp']:
        key = 'lec-' + suffix
        if key in bill:
            del bill[key]

    bill['data-collection-gbp'] += 5.89
    bill['settlement-gbp'] += 88

    triad.triad_bill(supply_source)
    tlms.hh(supply_source)
    bsuos.hh(supply_source)
    system_price.hh(supply_source)
    rates = supply_source.hh_rate(
        db_id, supply_source.finish_date, 'gsp_gbp_per_kwh')
    for slot_name in slot_names:
        slot_keys = slots[slot_name]
        bill[slot_keys['gbp']] = bill[slot_keys['gsp-kwh']] * rates[slot_name]

    for rate_name, rate_set in supply_source.supplier_rate_sets.iteritems():
        if len(rate_set) == 1:
            bill[rate_name] = rate_set.pop()

    bill['net-gbp'] = sum(v for k, v in bill.iteritems() if k[-4:] == '-gbp')
""",
            'properties': "{}", },
        'status_code': 303, },
    {
        'name': "Check that when there are gt 2 eras, the previous era is "
        "updated. Supply 1",
        'path': '/chellow/reports/307/output/',
        'method': 'post',
        'data': {
            'era_id': "15",
            'start_year': "2008",
            'start_month': "09",
            'start_day': "06",
            'start_hour': "00",
            'start_minute': "00",
            'is_ended': "false",
            'mop_contract_id': "57",
            'mop_account': "mc-22 0470 7514 535",
            'hhdc_contract_id': "53",
            'hhdc_account': "01",
            'msn': "",
            'pc_id': "9",
            'mtc_code': "845",
            'cop_id': "5",
            'ssc_code': "",
            'exp_llfc_code': "581",
            'exp_mpan_core': "22 0470 7514 535",
            'exp_sc': "150",
            'exp_supplier_contract_id': "55",
            'exp_supplier_account': "010", },
        'status_code': 303, },

    # Supply 1
    {
        'path': '/chellow/reports/307/output/?era_id=14',
        'regexes': [
            r'<select name="finish_day">\s*<option value="1">01</option>\s*'
            '<option value="2">02</option>\s*<option value="3">03</option>\s*'
            '<option value="4">04</option>\s*'
            '<option value="5" selected>05</option>', ], },
    {
        'name': "Check supplies snapshot",
        'path': '/chellow/reports/33/output/?year=2005&month=12',
        'status_code': 200,
        'regexes': [

            r'"2005-12-31 23:30","CI005","Wheal Rodney","","","11","net","",'
            '"22","LV","nhh","no","05","803","5","0154","2","MOP Contract",'
            '"mc-22 9974 3438 105","Dynamat data","dc-22 9974 3438 105",'
            '"K87D74429","2005-10-06 00:00","","","","","false","false",'
            '"false","false","false","false","22 9974 3438 105","20","540",'
            '"PC 5-8 & HH S/S","Non half-hourlies 2007","341665","","","","",'
            '"","","","","",""', ], },

    {
        'name': "Check supplies snapshot mandatory kw",
        'path': '/chellow/reports/33/output/?supply_id=1&year=2008&month=9&'
        'day=1&hour=00&minute=00',
        'status_code': 200,
        'regexes': [
            r'Date,Physical Site Id,Physical Site Name,Other Site Ids,'
            r'Other Site Names,Supply Id,Source,Generator Type,DNO Name,'
            r'Voltage Level,Metering Type,Mandatory HH,PC,MTC,CoP,SSC,'
            r'Number Of Registers,MOP Contract,Mop Account,HHDC Contract,'
            r'HHDC Account,Meter Serial Number,Meter Installation Date,'
            r'Latest Normal Meter Read Date,Latest Normal Meter Read Type,'
            r'Latest DC Bill Date,Latest MOP Bill Date,Import ACTIVE\?,'
            r'Import REACTIVE_IMPORT\?,Import REACTIVE_EXPORT\?,'
            r'Export ACTIVE\?,'
            r'Export REACTIVE_IMPORT\?,Export REACTIVE_EXPORT\?,'
            r'Import MPAN core,Import Agreed Supply Capacity \(kVA\),'
            r'Import LLFC Code,Import LLFC Description,'
            r'Import Supplier Contract,Import Supplier Account,'
            r'Import Mandatory kW,Latest Import Supplier Bill Date,'
            r'Export MPAN core,Export Agreed Supply Capacity \(kVA\),'
            r'Export LLFC Code,Export LLFC Description,'
            r'Export Supplier Contract,Export Supplier Account,'
            r'Export Mandatory kW,Latest Export Supplier Bill Date',

            r'"2008-09-30 23:30","CH017","Parbola","","","1","net","","22",'
            r'"LV","hh","no","00","845","5","","","MOP Contract",'
            r'"mc-22 0470 7514 535","HH contract","01","","2003-08-03 00:00",'
            r'"hh","","","","true","true","false","true","false","true","","",'
            r'"","","","","1.866","","22 0470 7514 535","150","581",'
            r'"Export \(LV\)","Half-hourlies 2007","010","",'
            r'"2007-02-28 23:30"']
        },

    {
        'name': "Generate an orphaned hh data message. Supply 5",
        'path': '/chellow/reports/307/output/',
        'method': 'post',
        'data': {
            'era_id': "5",
            'start_year': "2010",
            'start_month': "08",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00",
            'is_ended': "false",
            'msn': "",
            'pc_id': "9",
            'mtc_code': "845",
            'cop_id': "5",
            'ssc_code': "",
            'mop_contract_id': "57",
            'mop_account': "mc-22 0883 6932 301",
            'hhdc_contract_id': "53",
            'hhdc_account': "22 0883 6932 301",
            'imp_llfc_code': "570",
            'imp_mpan_core': "22 0883 6932 301",
            'imp_sc': "350",
            'imp_supplier_contract_id': "55",
            'imp_supplier_account': "01", },
        'status_code': 400,
        'regexes': [
            r"There are orphaned HH data between 2003-08-03 00:00 and "
            "2010-08-02 23:30\.", ], },

    # Generate similar one for ongoing orphaned data
    {
        'path': '/chellow/reports/307/output/',
        'method': 'post',
        'data': {
            'era_id': "5",
            'start_year': "2003",
            'start_month': "08",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00",
            'is_ended': "true",
            'finish_year': "2003",
            'finish_month': "08",
            'finish_day': "03",
            'finish_hour': "00",
            'finish_minute': "00",
            'msn': "",
            'pc_id': "9",
            'mtc_code': "845",
            'cop_id': "5",
            'ssc_code': "",
            'mop_contract_id': "57",
            'mop_account': "mc-22 0883 6932 301",
            'hhdc_contract_id': "53",
            'hhdc_account': "22 0883 6932 301",
            'imp_llfc_code': "570",
            'imp_mpan_core': "22 0883 6932 301",
            'imp_sc': "350",
            'imp_supplier_contract_id': "55",
            'imp_supplier_account': "01", },
        'status_code': 400,
        'regexes': [
            r"There are orphaned HH data between 2003-08-03 00:30 and "
            "ongoing\.", ], },

    # Test deleting of supplier contracts
    {
        'name': "Create a new supplier contract",
        'path': '/chellow/reports/315/output/',
        'method': 'post',
        'data': {
            'participant_id': "485",  # RWED
            'name': "GDF",
            'start_year': "2000",
            'start_month': "01",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00",
            'charge_script': "",
            'properties': "{}", },
        'regexes': [
            r"/reports/77/output/\?supplier_contract_id=60", ],
        'status_code': 303, },

    {
        'name': "Now delete the contract",
        'path': '/chellow/reports/317/output/',
        'method': 'post',
        'data': {
            'supplier_contract_id': "60",
            'delete': "Delete", },
        'status_code': 303, },

    {
        'name': "Check that it's really gone",
        'path': '/chellow/reports/317/output/?supplier_contract_id=60',
        'status_code': 404, },

    # Create an HHDC contract },
    {
        'name': "Test deleting of HHDC contracts",
        'path': '/chellow/reports/277/output/',
        'method': 'post',
        'data': {
            'participant_id': "527",  # UKDC
            'name': "Siemens Contract",
            'start_year': "2000",
            'start_month': "01",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00", },
        'status_code': 303,
        'regexes': [
            r"/chellow/reports/115/output/\?hhdc_contract_id=61", ], },

    # Now delete the contract
    {
        'path': '/chellow/reports/279/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "61",
            'delete': "Delete", },
        'status_code': 303, },

    # Check that it's really gone
    {
        'path': '/chellow/reports/115/output/?hhdc_contract_id=61',
        'status_code': 404, },

    # Load in march's HH data },
    {
        'name': "Check TRIAD calculation for March",
        'path': '/chellow/reports/293/output/',
        'method': 'post',
        'files': {'import_file': 'hh_data_long.csv'},
        'status_code': 303,
        'regexes': [
            r"/reports/295/output/\?process_id=12", ], },
    {
        'path': '/chellow/reports/295/output/?process_id=12',
        'tries': {'max': 10, 'period': 1},
        'status_code': 200,
        'regexes': [
            r"The file has been imported successfully\.", ], },

    # Create the virtual bill
    {
        'path': '/chellow/reports/265/output/',
        'method': 'post',
        'data': {
            'is_core': "false",
            'name': "TRIAD Estimates",
            'start_year': "2000",
            'start_month': "01",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00", },
        'regexes': [
            r"/reports/267/output/\?non_core_contract_id=62", ],
        'status_code': 303, },

    # Edit the rate script
    {
        'path': '/chellow/reports/273/output/',
        'method': 'post',
        'data': {
            'rate_script_id': "315",
            'start_year': "2000",
            'start_month': "01",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00",
            'script': """
def triad_estimates():
    return {}
"""},
        'status_code': 303, },
    {
        'path': '/chellow/reports/291/output/?supply_id=7&start_year=2009&'
        'start_month=03&start_day=01&start_hour=00&start_minute=0&'
        'finish_year=2009&finish_month=03&finish_day=31&finish_hour=23&'
        'finish_minute=30',
        'status_code': 200,
        'regexes': [
            r'"Imp MPAN Core","Exp MPAN Core","Site Code","Site Name",'
            '"Account","From","To","","mop-net-gbp","mop-problem","",'
            '"dc-net-gbp","dc-problem","","imp-supplier-net-gbp",'
            '"imp-supplier-tlm","imp-supplier-ccl-kwh",'
            '"imp-supplier-ccl-rate","imp-supplier-ccl-gbp",'
            '"imp-supplier-data-collection-gbp",'
            '"imp-supplier-duos-availability-kva",'
            '"imp-supplier-duos-availability-days",'
            '"imp-supplier-duos-availability-rate",'
            '"imp-supplier-duos-availability-gbp",'
            '"imp-supplier-duos-excess-availability-kva",'
            '"imp-supplier-duos-excess-availability-days",'
            '"imp-supplier-duos-excess-availability-rate",'
            '"imp-supplier-duos-excess-availability-gbp",'
            '"imp-supplier-duos-day-kwh","imp-supplier-duos-day-gbp",'
            '"imp-supplier-duos-night-kwh","imp-supplier-duos-night-gbp",'
            '"imp-supplier-duos-reactive-rate",'
            '"imp-supplier-duos-reactive-gbp",'
            '"imp-supplier-duos-standing-gbp","imp-supplier-settlement-gbp",'
            '"imp-supplier-night-msp-kwh","imp-supplier-night-gsp-kwh",'
            '"imp-supplier-night-gbp","imp-supplier-other-msp-kwh",'
            '"imp-supplier-other-gsp-kwh","imp-supplier-other-gbp",'
            '"imp-supplier-summer-pk-msp-kwh",'
            '"imp-supplier-summer-pk-gsp-kwh","imp-supplier-summer-pk-gbp",'
            '"imp-supplier-winter-low-pk-msp-kwh",'
            '"imp-supplier-winter-low-pk-gsp-kwh",'
            '"imp-supplier-winter-low-pk-gbp",'
            '"imp-supplier-winter-off-pk-msp-kwh",'
            '"imp-supplier-winter-off-pk-gsp-kwh",'
            '"imp-supplier-winter-off-pk-gbp",'
            '"imp-supplier-winter-pk-msp-kwh",'
            '"imp-supplier-winter-pk-gsp-kwh","imp-supplier-winter-pk-gbp",'
            '"imp-supplier-bsuos-kwh","imp-supplier-bsuos-rate",'
            '"imp-supplier-bsuos-gbp","imp-supplier-triad-actual-1-date",'
            '"imp-supplier-triad-actual-1-msp-kw",'
            '"imp-supplier-triad-actual-1-status",'
            '"imp-supplier-triad-actual-1-laf",'
            '"imp-supplier-triad-actual-1-gsp-kw",'
            '"imp-supplier-triad-actual-2-date",'
            '"imp-supplier-triad-actual-2-msp-kw",'
            '"imp-supplier-triad-actual-2-status",'
            '"imp-supplier-triad-actual-2-laf",'
            '"imp-supplier-triad-actual-2-gsp-kw",'
            '"imp-supplier-triad-actual-3-date",'
            '"imp-supplier-triad-actual-3-msp-kw",'
            '"imp-supplier-triad-actual-3-status",'
            '"imp-supplier-triad-actual-3-laf",'
            '"imp-supplier-triad-actual-3-gsp-kw",'
            '"imp-supplier-triad-actual-gsp-kw",'
            '"imp-supplier-triad-actual-rate",'
            '"imp-supplier-triad-actual-gbp",'
            '"imp-supplier-triad-estimate-1-date",'
            '"imp-supplier-triad-estimate-1-msp-kw",'
            '"imp-supplier-triad-estimate-1-status",'
            '"imp-supplier-triad-estimate-1-laf",'
            '"imp-supplier-triad-estimate-1-gsp-kw",'
            '"imp-supplier-triad-estimate-2-date",'
            '"imp-supplier-triad-estimate-2-msp-kw",'
            '"imp-supplier-triad-estimate-2-status",'
            '"imp-supplier-triad-estimate-2-laf",'
            '"imp-supplier-triad-estimate-2-gsp-kw",'
            '"imp-supplier-triad-estimate-3-date",'
            '"imp-supplier-triad-estimate-3-msp-kw",'
            '"imp-supplier-triad-estimate-3-status",'
            '"imp-supplier-triad-estimate-3-laf",'
            '"imp-supplier-triad-estimate-3-gsp-kw",'
            '"imp-supplier-triad-estimate-gsp-kw",'
            '"imp-supplier-triad-estimate-rate",'
            '"imp-supplier-triad-estimate-months",'
            '"imp-supplier-triad-estimate-gbp",'
            '"imp-supplier-triad-all-estimates-months",'
            '"imp-supplier-triad-all-estimates-gbp"'
            ',"imp-supplier-problem"',
            r'"22 4862 4512 332","","CH023","Treglisson","11640077",'
            '"2009-03-01 00:00","2009-03-31 23:30","","0","","","0","","",'
            '"10614.4095537","","148925.71","0.00456","679.1012376","5.89",'
            '"230","31","0.0368","262.384","169.72","31","0.0368",'
            '"193.616576","105487.44","770.058312","43438.27","112.939502",'
            '"0.0033","0.0","","88","43401.25","46092.1275","288.794834064",'
            '"54364.73","57735.34326","361.74656673","0","0","0.0","0","0",'
            '"0.0","51159.73","54331.63326","340.420281354","0","0","0.0",'
            '"159627.381103","","146.91999205","2009-01-06 17:00","288.82",'
            '"A","1.07","309.0374","2008-12-01 17:00","384.44","A","1.07",'
            '"411.3508","2008-12-15 17:00","185.36","A","1.07","198.3352",'
            '"306.241133333","25.212997","7721.25677601","2007-12-17 17:00",'
            '"0","X","1.07","0.0","2008-01-03 17:00","43.6","A","1.062",'
            '"46.3032","2007-11-26 17:00","0","X","1.07","0.0","15.4344",'
            '"25.212997","1","32.4289567414","12","-389.147480897",""',
            r"text/csv",
            r"supply_virtual_bills_7.csv", ], },

    # Try looking at it using the TRIAD report
    {
        'path': '/chellow/reports/41/output/?supply_id=4&year=2010',
        'status_code': 200,
        'regexes': [
            r'CI005,"Wheal Rodney","1",net,"","22 6158 2968 220",'
            '"2010-01-07 17:00","0","X","1.058","0.0","2010-01-25 17:00","0",'
            '"X","1.058","0.0","2009-12-15 17:00","0","X","1.058","0.0","0.0",'
            '"25.631634","0.0","22 3479 7618 470","2010-01-07 17:00","0","X",'
            '"1.058","0.0","2010-01-25 17:00","0","X","1.058","0.0",'
            '"2009-12-15 17:00","0","X","1.058","0.0","0.0","25.631634",'
            '"0.0"', ], },
    {
        'name': "Check we can delete a rate script (when it's not the only "
        "one). Supplier contract 59.",
        'path': '/chellow/reports/319/output/',
        'method': 'post',
        'data': {
            'supplier_rate_script_id': "311",
            'delete': "Delete", },
        'status_code': 303, },
    {
        'name': "Try 'Supply MPAN Months' report.",
        'path': '/chellow/reports/15/output/?supply_id=2&is_import=true&'
        'year=2014&years=1',
        'regexes': [
            r"&gt;\s*Import\s*data by month", ],
        'status_code': 200, },
    {
        'name': "Try 'Supply Raw HH Data' report.",
        'path': '/chellow/reports/17/output/?supply_id=1&months=1&'
        'finish_year=2008&finish_month=07',
        'regexes': [
            r'<option value="07" selected>07</option>', ],
        'status_code': 200, },
    {
        'name': "Try site graph report.",
        'path': '/chellow/reports/21/output/?site_id=7&finish_year=2008&'
        'finish_month=7&months=1',
        'status_code': 200, },
    {
        'name': "Try era graph report.",
        'path': '/chellow/reports/23/output/?site_id=7&finish_year=2008&'
        'finish_month=7&months=1',
        'status_code': 200, },
    {
        'name': "Try 'Site HH bulk figures' report.",
        'path': '/chellow/reports/29/output/?site_id=5&type=used&months=1&'
        'finish_year=2008&finish_month=01',
        'regexes': [
            r"CH023,used,2008-01-01,3.77", ],
        'status_code': 200, },
    {
        'name': "Try HHDC virtual bills.",
        'path': '/chellow/reports/81/output/?hhdc_contract_id=53&months=1&'
        'end_year=2008&end_month=7',
        'status_code': 200,
        'regexes': [
            r"Import MPAN Core, Export MPAN Core, Start Date, Finish Date,"
            "net-gbp",
            r'22 9205 6799 106,22 0470 7514 535,2008-07-01 00:00,'
            '2008-07-06 23:30,"0",',
            r'attachment; filename="hhdc_vbs.csv"', ], },

    # Can we make a supply have source sub and view site level hh data okay?
    {
        'name': "CSV Sites HH Data",
        'path': '/chellow/reports/305/output/',
        'method': 'post',

        # Can we update a supply name?

        # Can we update a supply source?
        'data': {
            'supply_id': "1",
            'name': "Hello",
            'source_id': "2",
            'generator_type_id': "1",
            'gsp_group_id': "11", },
        'regexes': [
            r"/reports/7/output/\?supply_id=1", ],
        'status_code': 303, },
    {
        'path': '/chellow/reports/183/output/?start_year=2008&start_month=07&'
        'start_day=1&start_hour=0&start_minute=0&finish_year=2008&'
        'finish_month=07&finish_day=31&finish_hour=23&finish_minute=30',
        'status_code': 200, },
    {
        'name': "CSV Supplies Duration",
        'path': '/chellow/reports/149/output/?start_year=2009&start_month=03&'
        'start_day=1&start_hour=0&start_minute=0&finish_year=2009&'
        'finish_month=03&finish_day=31&finish_hour=23&finish_minute=30',
        'regexes': [
            r'"7","1","net","","CH023","Treglisson","2009-03-01 00:00",'
            '"2009-03-31 23:30","00","845","5","","0","hh",540,'
            '22 4862 4512 332,230,Half-hourlies 2007,148925.71,0,158159.10402,'
            '399.72,2009-03-13 08:00,None,0,,,,,0,0,,0,,None,1488', ], },

    # Insert rate script },
    {
        'name': "Manipulate dno contracts",
        'path': '/chellow/reports/243/output/',
        'method': 'post',
        'data': {
            'dno_contract_id': "37",

            # DNO 10
            'start_year': "2010",
            'start_month': "05",
            'start_day': "01",
            'start_hour': "00",
            'start_minute': "00", },
        'regexes': [
            r"/chellow/reports/69/output/\?dno_rate_script_id=316", ],
        'status_code': 303, },

    # Test bad syntax gives an error
    {
        'path': '/chellow/reports/285/output/',
        'method': 'post',
        'data': {
            'dno_rate_script_id': "316",
            'start_year': "2010",
            'start_month': "05",
            'start_day': "01",
            'start_hour': "00",
            'start_minute': "00",
            'script': "{{/0erk",
            'update': "Update", },
        'status_code': 400, },

    # Delete rate script
    {
        'path': '/chellow/reports/285/output/',
        'method': 'post',
        'data': {
            'dno_rate_script_id': "316",
            'delete': "Delete", },
        'status_code': 303, },
    {
        'name': "CSV Sites Monthly Duration",
        'path': '/chellow/reports/161/output/?site_id=5&months=1&'
        'finish_year=2009&finish_month=03',
        'status_code': 303, },
    {
        'path': '/chellow/reports/251/output/',
        'tries': {'max': 40, 'period': 1},
        'regexes': [
            r"FINISHED_site_monthly_duration_for_CH023_1_to_2009_3\.csv", ],
        'status_code': 200, },
    {
        'name': "CSV Sites TRIAD",
        'path': '/chellow/reports/181/output/?site_id=3&year=2010',
        'regexes': [
            "Site Code,",
            '"CI005","Wheal Rodney",2010-01-07 17:00,'],
        'status_code': 200},

    # See if it handles the case where there isn't an import virtual bill
    # function.
    {
        'name': "CSV Sites Monthly Duration",
        'path': '/chellow/reports/161/output/?site_id=4&months=1&'
        'finish_year=2009&finish_month=04',
        'status_code': 303, },
    {
        'path': '/chellow/reports/251/output/',
        'tries': {'max': 20, 'period': 1},
        'regexes': [
            r"FINISHED_site_monthly_duration_for_CI017_1_to_2009_4\.csv", ],
        'status_code': 200, },
    {
        'path': '/chellow/reports/253/output/?'
        'name=FINISHED_site_monthly_duration_for_CI017_1_to_2009_4.csv',
        'tries': {'max': 10, 'period': 1},
        'status_code': 200,
        'regexes': [
            r"Site Id,Site Name,Associated Site Ids,Sources,Generator Types,"
            "Month,Metered Imported kWh,Metered Displaced kWh,"
            "Metered Exported kWh,Metered Used kWh,Metered Parasitic kWh,"
            "Metered Generated kWh,Metered 3rd Party Import kWh,"
            "Metered 3rd Party Export kWh,Metered Imported GBP,"
            "Metered Displaced GBP,Metered Exported GBP,Metered Used GBP,"
            "Metered 3rd Party Import GBP,Billed Imported kWh,"
            "Billed Imported GBP,Metering Type,Problem",
            r'"CI017","Roselands","","net","","2009-04-30 23:30","0","0","0",'
            '"0","0","0","0","0","2784.89","0","0","2784.89","0","0","0","hh",'
            '"'
            "Can't find the virtual_bill function in the supplier "
            'contract. "', ], },

    # Update the supplier contract
    {
        'path': '/chellow/reports/317/output/',
        'method': 'post',
        'data': {
            'supplier_contract_id': "58",
            'party_id': "22",  # BIZZ
            'name': "Half-hourlies 2013",
            'charge_script': """
from net.sf.chellow.monad import Monad
import datetime
from dateutil.relativedelta import relativedelta
import pytz
from sqlalchemy import or_

Monad.getUtils()['impt'](
    globals(), 'computer', 'db', 'utils', 'computer', 'triad', 'ccl', 'bsuos',
    'tlms', 'duos', 'rcrc', 'aahedc')


def virtual_bill_titles():
    return [
        'net-gbp', 'tlm', 'ccl-kwh', 'ccl-rate', 'ccl-gbp',
        'data-collection-gbp', 'duos-availability-kva',
        'duos-availability-days', 'duos-availability-rate',
        'duos-availability-gbp', 'duos-excess-availability-kva',
        'duos-excess-availability-days', 'duos-excess-availability-rate',
        'duos-excess-availability-gbp','duos-green-kwh', 'duos-green-rate',
        'duos-green-gbp', 'duos-green-kwh', 'duos-green-rate',
        'duos-amber-gbp', 'duos-amber-kwh', 'duos-red-rate', 'duos-red-gbp',
        'duos-reactive-kvarh', 'duos-reactive-rate', 'duos-reactive-gbp',
        'duos-fixed-days', 'duos-fixed-rate', 'duos-fixed-gbp',
        'settlement-gbp', 'aahedc-msp-kwh', 'aahedc-gsp-kwh', 'aahedc-rate',
        'aahedc-gbp', 'rcrc-kwh', 'rcrc-rate', 'rcrc-gbp', 'night-msp-kwh',
        'night-gsp-kwh', 'night-gbp', 'other-msp-kwh', 'other-gsp-kwh',
        'other-gbp', 'summer-pk-msp-kwh', 'summer-pk-gsp-kwh', 'summer-pk-gbp',
        'winter-low-pk-msp-kwh', 'winter-low-pk-gsp-kwh', 'winter-low-pk-gbp',
        'winter-off-pk-msp-kwh', 'winter-off-pk-gsp-kwh', 'winter-off-pk-gbp',
        'winter-pk-msp-kwh', 'winter-pk-gsp-kwh', 'winter-pk-gbp', 'bsuos-kwh',
        'bsuos-rate', 'bsuos-gbp', 'triad-actual-1-date',
        'triad-actual-1-msp-kw', 'triad-actual-1-status', 'triad-actual-1-laf',
        'triad-actual-1-gsp-kw', 'triad-actual-2-date',
        'triad-actual-2-msp-kw', 'triad-actual-2-status', 'triad-actual-2-laf',
        'triad-actual-2-gsp-kw', 'triad-actual-3-date',
        'triad-actual-3-msp-kw', 'triad-actual-3-status', 'triad-actual-3-laf',
        'triad-actual-3-gsp-kw', 'triad-actual-gsp-kw', 'triad-actual-rate',
        'triad-actual-gbp', 'triad-estimate-1-date', 'triad-estimate-1-msp-kw',
        'triad-estimate-1-status', 'triad-estimate-1-laf',
        'triad-estimate-1-gsp-kw', 'triad-estimate-2-date',
        'triad-estimate-2-msp-kw', 'triad-estimate-2-status',
        'triad-estimate-2-laf', 'triad-estimate-2-gsp-kw',
        'triad-estimate-3-date', 'triad-estimate-3-msp-kw',
        'triad-estimate-3-status', 'triad-estimate-3-laf',
        'triad-estimate-3-gsp-kw', 'triad-estimate-gsp-kw',
        'triad-estimate-rate', 'triad-estimate-months', 'triad-estimate-gbp',
        'triad-all-estimates-months', 'triad-all-estimates-gbp', 'problem']

def displaced_virtual_bill_titles():
    return [
        'bsuos-kwh', 'bsuos-rate', 'bsuos-gbp', 'ccl-kwh', 'ccl-rate',
        'ccl-gbp', 'duos-day-gbp', 'duos-day-kwh', 'duos-night-gbp',
        'duos-night-kwh', 'duos-reactive-gbp', 'duos-reactive-working',
        'net-gbp', 'duos-standing-gbp', 'night-gbp', 'night-gsp-kwh',
        'night-msp-kwh', 'other-gbp', 'other-gsp-kwh', 'other-msp-kwh',
        'summer-pk-gbp', 'summer-pk-gsp-kwh', 'summer-pk-msp-kwh', 'triad-gbp',
        'triad-working', 'winter-low-pk-gbp', 'winter-low-pk-gsp-kwh',
        'winter-low-pk-msp-kwh', 'winter-off-pk-gbp', 'winter-off-pk-gsp-kwh',
        'winter-off-pk-msp-kwh', 'winter-pk-gbp', 'winter-pk-gsp-kwh',
        'winter-pk-msp-kwh']

slot_names = [
    'winter-pk', 'winter-low-pk', 'winter-off-pk', 'summer-pk', 'night',
    'other']

slots = {}
for slot_name in slot_names:
    slots[slot_name] = {
        'msp-kwh': slot_name + '-msp-kwh', 'gsp-kwh': slot_name + '-gsp-kwh',
        'gbp': slot_name + '-gbp'}


def displaced_virtual_bill(supply_source):
    bill = supply_source.supplier_bill

    supply_source.is_green = False
    duos.duos_vb(supply_source)

    for datum in supply_source.hh_data:
        is_weekday = datum['start-date'].weekday() < 5
        if is_weekday and datum['utc-month'] in (1, 12) and \
                16 < datum['utc-decimal-hour'] <= 19:
            slot_key = 'winter-pk'
        elif is_weekday and datum['utc-month'] in (2, 11) and \
                16 < datum['utc-decimal-hour'] <= 19:
            slot_key = 'winter-low-pk'
        elif is_weekday and \
                (datum['utc-month'] > 10 or datum['utc-month'] < 4) and \
                8 < datum['utc-decimal-hour'] <= 20:
            slot_key = 'winter-off-pk'
        elif is_weekday and \
                (datum['utc-month'] > 3 or datum['utc-month'] < 11) and \
                8 < datum['utc-decimal-hour'] <= 20:
            slot_key = 'summer-pk'
        elif 0 < datum['utc-decimal-hour'] <= 7:
            slot_key = 'night'
        else:
            slot_key = 'other'
        slot_keys = slots[slot_key]
        bill[slot_keys['msp-kwh']] += datum['msp-kwh']
        bill[slot_keys['gsp-kwh']] += datum['gsp-kwh']

    ccl.ccl(supply_source)

    for suffix in ['kwh', 'rate', 'gbp']:
        key = 'lec-' + suffix
        if key in bill:
            del bill[key]

    triad.triad_bill(supply_source)
    tlms.hh(supply_source)
    bsuos.hh(supply_source)
    aahedc.hh(supply_source)

    rates = supply_source.hh_rate(
        db_id, supply_source.finish_date, 'gsp_gbp_per_kwh')
    for slot_name in slot_names:
        slot_keys = slots[slot_name]
        bill[slot_keys['gbp']] = bill[slot_keys['gsp-kwh']] * rates[slot_name]

    for rate_name, rate_set in supply_source.supplier_rate_sets.iteritems():
        if len(rate_set) == 1:
            bill[rate_name] = rate_set.pop()

    bill['net-gbp'] = sum(v for k, v in bill.iteritems() if k[-4:] == '-gbp')


def virtual_bill(supply_source):
    duos.duos_vb(supply_source)
    ccl.ccl(supply_source)
    triad.triad_bill(supply_source)
    tlms.hh(supply_source)
    rcrc.hh(supply_source)
    bsuos.hh(supply_source)
    aahedc.hh(supply_source)

    bill = supply_source.supplier_bill
    supply_source.is_green = False

    for datum in supply_source.hh_data:
        is_weekday = datum['utc-day-of-week'] < 5
        if is_weekday and datum['utc-month'] in (1, 12) and \
                16 < datum['utc-decimal-hour'] <= 19:
            slot_key = 'winter-pk'
        elif is_weekday and datum['utc-month'] in (2, 11) and \
                16 < datum['utc-decimal-hour'] <= 19:
            slot_key = 'winter-low-pk'
        elif is_weekday and \
                (datum['utc-month'] > 10 or datum['utc-month'] < 4) and \
                8 < datum['utc-decimal-hour'] <= 20:
            slot_key = 'winter-off-pk'
        elif is_weekday and \
                (datum['utc-month'] > 3 or datum['utc-month'] < 11) and \
                8 < datum['utc-decimal-hour'] <= 20:
            slot_key = 'summer-pk'
        elif 0 < datum['utc-decimal-hour'] <= 7:
            slot_key = 'night'
        else:
            slot_key = 'other'
        slot_keys = slots[slot_key]
        bill[slot_keys['msp-kwh']] += datum['msp-kwh']
        bill[slot_keys['gsp-kwh']] += datum['gsp-kwh']
        rates = supply_source.hh_rate(
            db_id, datum['start-date'], 'gsp_gbp_per_kwh')
        bill[slot_keys['gbp']] += datum['gsp-kwh'] * rates[slot_name]

    for suffix in ['kwh', 'rate', 'gbp']:
        key = 'lec-' + suffix
        if key in bill:
            del bill[key]

    bill['data-collection-gbp'] += 5.89
    bill['settlement-gbp'] += 88

    for rate_name, rate_set in supply_source.supplier_rate_sets.iteritems():
        if len(rate_set) == 1:
            bill[rate_name] = rate_set.pop()

    bill['net-gbp'] = sum(v for k, v in bill.iteritems() if k[-4:] == '-gbp')
""",
            'properties': "{}", },
        'status_code': 303,
        'regexes': [
            r"/reports/77/output/\?supplier_contract_id=58", ], },
    {
        'path': '/chellow/reports/317/output/',
        'method': 'post',
        'data': {
            'supplier_contract_id': "59",
            'name': "Non half-hourlies 2007",
            'party_id': "664",  # HYDE
            'charge_script': """
def virtual_bill_titles():
    return ['net-gbp', 'vat-gbp', 'gross-gbp', 'sum-msp-kwh', 'problem']


def virtual_bill(supply_source):
    bill = supply_source.supplier_bill
    sum_msp_kwh = sum(h['msp-kwh'] for h in supply_source.hh_data)

    for rate_name, rate_set in supply_source.supplier_rate_sets.iteritems():
        if len(rate_set) == 1:
            bill[rate_name] = rate_set.pop()

    bill.update(
        {
            'net-gbp': 0.0, 'vat-gbp':0.0, 'gross-gbp': 0.0,
            'sum-msp-kwh': sum_msp_kwh})
""",
            'properties': "{}", },
        'status_code': 303, },
    {
        'name': "Set configuration properties",
        'path': '/chellow/reports/269/output/',
        'method': 'post',
        'data': {
            'non_core_contract_id': "13",
            'name': "configuration",
            'charge_script': "",
            'properties': """
{
    'ips': {'127.0.0.1': 'implicit-user@localhost'},
    'site_links': [
        {'name': 'Google Maps', 'href': 'https://maps.google.com/maps?q='}]}
""", },
        'status_code': 303, },
    {
        'name': "Site In View World",
        'path': '/chellow/reports/5/output/?site_id=3',
        'status_code': 200,
        'regexes': [
            r'<a href="/chellow/reports/7/output/\?supply_id=2">view</a>',
            r'<a href="https://maps.google.com/maps\?q=CI005">Google Maps</a>',
            r'<option value="imp_net">Imported</option>', ], },

    # Check that it shows a dead supply properly. Supply 11
    {
        'path': '/chellow/reports/307/output/',
        'method': 'post',
        'data': {
            'era_id': "11",
            'start_year': "2005",
            'start_month': "10",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00",
            'is_ended': "true",
            'finish_year': "2010",
            'finish_month': "04",
            'finish_day': "13",
            'finish_hour': "23",
            'finish_minute': "30",
            'mop_contract_id': "57",
            'mop_account': "mc-22 9974 3438 105",
            'hhdc_contract_id': "53",
            'hhdc_account': "dc-22 9974 3438 105",
            'msn': "K87D74429",
            'pc_id': "5",
            'mtc_code': "803",
            'cop_id': "5",
            'ssc_code': "0154",
            'imp_llfc_code': "540",
            'imp_mpan_core': "22 9974 3438 105",
            'imp_sc': "20",
            'imp_supplier_contract_id': "59",
            'imp_supplier_account': "SA341665", },
        'status_code': 303, },
    {
        'path': '/chellow/reports/5/output/?site_id=3',
        'status_code': 200,
        'regexes': [
            r'<td>\s*'
            '<a href="/chellow/reports/7/output/\?supply_id=11">view</a>\s*'
            '</td>\s*<td>3</td>\s*<td>2005-10-03 00:00</td>\s*<td>\s*'
            '2010-04-13 23:30\s*</td>', ], },

    # Insert a 20 supply },
    {
        'name': "Try a pre 2010-04-01 DNO 20 bill.",
        'path': '/chellow/reports/311/output/',
        'method': 'post',
        'data': {
            'site_id': "1",
            'source_id': "1",
            'name': "Reserve Supply",
            'start_year': "2003",
            'start_month': "08",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00",
            'msn': "",
            'gsp_group_id': "8",
            'pc_id': "9",
            'mtc_code': "845",
            'cop_id': "5",
            'ssc_code': "",
            'mop_contract_id': "57",
            'mop_account': "mc-22 6354 2983 570",
            'hhdc_contract_id': "54",
            'hhdc_account': "01",
            'imp_llfc_code': "453",
            'imp_mpan_core': "20 6354 2983 571",
            'imp_sc': "2300",
            'imp_supplier_contract_id': "55",
            'imp_supplier_account': "141 5532",
            'insert': "insert", },
        'regexes': [
            r"/reports/7/output/\?supply_id=12", ],
        'status_code': 303, },

    # Add import related ACTIVE channel. Supply 12
    {
        'path': '/chellow/reports/299/output/',
        'method': 'post',
        'data': {
            'era_id': "16",
            'imp_related': "true",
            'channel_type': "ACTIVE", },
        'regexes': [
            r"/chellow/reports/301/output/\?channel_id=42", ],
        'status_code': 303, },

    # Try out simple.csv hh import format.
    {
        'path': '/chellow/reports/211/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "54", },
        'files': {'import_file': 'hh.simple.csv'},
        'status_code': 303,
        'regexes': [
            r"/reports/65/output/\?hhdc_contract_id=54&process_id=0", ], },
    {
        'path': '/chellow/reports/65/output/?hhdc_contract_id=54&process_id=0',
        'tries': {'max': 10, 'period': 1},
        'regexes': [
            r"The import has completed.*successfully.", ],
        'status_code': 200, },

    # Check that the first datum has been correctly loaded in
    {
        'path': '/chellow/reports/17/output/?supply_id=7&months=1&'
        'finish_year=2010&finish_month=02',
        'regexes': [
            r"<td>\s*2010-02-04 20:00\s*</td>\s*<td>30.4339</td>", ],
        'status_code': 200, },
    {
        'path': '/chellow/reports/291/output/?supply_id=12&start_year=2009&'
        'start_month=3&start_day=01&start_hour=00&start_minute=0&'
        'finish_year=2009&finish_month=03&finish_day=31&finish_hour=23&'
        'finish_minute=30',
        'status_code': 200,
        'regexes': [
            r'"Imp MPAN Core","Exp MPAN Core","Site Code","Site Name",'
            '"Account","From","To","","mop-net-gbp","mop-problem","",'
            '"dc-net-gbp","dc-problem","","imp-supplier-net-gbp",'
            '"imp-supplier-tlm","imp-supplier-ccl-kwh",'
            '"imp-supplier-ccl-rate","imp-supplier-ccl-gbp",'
            '"imp-supplier-data-collection-gbp",'
            '"imp-supplier-duos-availability-kva",'
            '"imp-supplier-duos-availability-days",'
            '"imp-supplier-duos-availability-rate",'
            '"imp-supplier-duos-availability-gbp",'
            '"imp-supplier-duos-excess-availability-kva",'
            '"imp-supplier-duos-excess-availability-days",'
            '"imp-supplier-duos-excess-availability-rate",'
            '"imp-supplier-duos-excess-availability-gbp",'
            '"imp-supplier-duos-day-kwh","imp-supplier-duos-day-gbp",'
            '"imp-supplier-duos-night-kwh","imp-supplier-duos-night-gbp",'
            '"imp-supplier-duos-reactive-rate",'
            '"imp-supplier-duos-reactive-gbp",'
            '"imp-supplier-duos-standing-gbp","imp-supplier-settlement-gbp",'
            '"imp-supplier-night-msp-kwh","imp-supplier-night-gsp-kwh",'
            '"imp-supplier-night-gbp","imp-supplier-other-msp-kwh",'
            '"imp-supplier-other-gsp-kwh","imp-supplier-other-gbp",'
            '"imp-supplier-summer-pk-msp-kwh",'
            '"imp-supplier-summer-pk-gsp-kwh","imp-supplier-summer-pk-gbp",'
            '"imp-supplier-winter-low-pk-msp-kwh",'
            '"imp-supplier-winter-low-pk-gsp-kwh",'
            '"imp-supplier-winter-low-pk-gbp",'
            '"imp-supplier-winter-off-pk-msp-kwh",'
            '"imp-supplier-winter-off-pk-gsp-kwh",'
            '"imp-supplier-winter-off-pk-gbp",'
            '"imp-supplier-winter-pk-msp-kwh",'
            '"imp-supplier-winter-pk-gsp-kwh","imp-supplier-winter-pk-gbp",'
            '"imp-supplier-bsuos-kwh","imp-supplier-bsuos-rate",'
            '"imp-supplier-bsuos-gbp","imp-supplier-triad-actual-1-date",'
            '"imp-supplier-triad-actual-1-msp-kw",'
            '"imp-supplier-triad-actual-1-status",'
            '"imp-supplier-triad-actual-1-laf",'
            '"imp-supplier-triad-actual-1-gsp-kw",'
            '"imp-supplier-triad-actual-2-date",'
            '"imp-supplier-triad-actual-2-msp-kw",'
            '"imp-supplier-triad-actual-2-status",'
            '"imp-supplier-triad-actual-2-laf",'
            '"imp-supplier-triad-actual-2-gsp-kw",'
            '"imp-supplier-triad-actual-3-date",'
            '"imp-supplier-triad-actual-3-msp-kw",'
            '"imp-supplier-triad-actual-3-status",'
            '"imp-supplier-triad-actual-3-laf",'
            '"imp-supplier-triad-actual-3-gsp-kw",'
            '"imp-supplier-triad-actual-gsp-kw",'
            '"imp-supplier-triad-actual-rate",'
            '"imp-supplier-triad-actual-gbp",'
            '"imp-supplier-triad-estimate-1-date",'
            '"imp-supplier-triad-estimate-1-msp-kw",'
            '"imp-supplier-triad-estimate-1-status",'
            '"imp-supplier-triad-estimate-1-laf",'
            '"imp-supplier-triad-estimate-1-gsp-kw",'
            '"imp-supplier-triad-estimate-2-date",'
            '"imp-supplier-triad-estimate-2-msp-kw",'
            '"imp-supplier-triad-estimate-2-status",'
            '"imp-supplier-triad-estimate-2-laf",'
            '"imp-supplier-triad-estimate-2-gsp-kw",'
            '"imp-supplier-triad-estimate-3-date",'
            '"imp-supplier-triad-estimate-3-msp-kw",'
            '"imp-supplier-triad-estimate-3-status",'
            '"imp-supplier-triad-estimate-3-laf",'
            '"imp-supplier-triad-estimate-3-gsp-kw",'
            '"imp-supplier-triad-estimate-gsp-kw",'
            '"imp-supplier-triad-estimate-rate",'
            '"imp-supplier-triad-estimate-months",'
            '"imp-supplier-triad-estimate-gbp",'
            '"imp-supplier-triad-all-estimates-months",'
            '"imp-supplier-triad-all-estimates-gbp",'
            '"imp-supplier-problem"',
            r'"20 6354 2983 571","","CI004","Lower Treave","141 5532",'
            '"2009-03-01 00:00","2009-03-31 23:30","","0","","","0","","",'
            '"2274.51858148","","","0.00456","","5.89","2300","","",'
            '"2165.0","0","","","","0","0.0","86.9732","0.102628376","","",'
            '"14.91","88","86.9732","93.49619","0.585809728064","0","0.0",'
            '"0.0",'
            '"0","0","0.0","0","0","0.0","0","0.0","0.0","0","0","0.0",'
            '"94.2952925863","","0.0301433761811",'
            '"2009-01-06 17:00","0","X","1.095","0.0","2008-12-01 17:00","0",'
            '"X","1.095","0.0","2008-12-15 17:00","0","X","1.095","0.0",'
            '"0.0","22.19481","0.0","2007-12-17 17:00","0","X","1.095","0.0",'
            '"2008-01-03 17:00","0","X","1.079","0.0","2007-11-26 17:00","0",'
            '"X","1.095","0.0","0.0","22.19481","1","0.0","12","-0.0",""'], },

    # Check it works when the DNO rate script contains a double LLFC 453,470
    {
        'path': '/chellow/reports/291/output/?supply_id=12&start_year=2009&'
        'start_month=6&start_day=01&start_hour=00&start_minute=0&'
        'finish_year=2009&finish_month=06&finish_day=30&finish_hour=23&'
        'finish_minute=30',
        'regexes': [
            r'"20 6354 2983 571","","CI004","Lower Treave","141 5532",'
            '"2009-06-01 00:00","2009-06-30 23:30",', ],
        'status_code': 200, },

    # supply 12, era 16, channel 42
    {
        'path': '/chellow/reports/309/output/?hh_datum_id=6773',
        'method': 'post',
        'data': {
            'delete': "Delete", },
        'status_code': 303, },
    {
        'name': "Delete a supply.",
        'path': '/chellow/reports/305/output/',
        'method': 'post',
        'data': {
            'supply_id': "12",
            'delete': "Delete", },
        'status_code': 303, },

    # Create new supplier contract },
    {
        'name': "Test importing of sse.edi bills",
        'path': '/chellow/reports/315/output/',
        'method': 'post',
        'data': {
            'participant_id': "54",  # COOP
            'name': "Non half-hourlies 2010",
            'start_year': "2000",
            'start_month': "01",
            'start_day': "01",
            'start_hour': "00",
            'start_minute': "00",
            'charge_script': """
def virtual_bill_titles():
    return ['net-gbp', 'sum-msp-kwh', 'problem']

def virtual_bill(supply_source):
    sum_msp_kwh = sum(h['msp-kwh'] for h in supply_source.hh_data)
    bill = supply_source.supplier_bill
    for rate_name, rate_set in supply_source.supplier_rate_sets.iteritems():
        if len(rate_set) == 1:
            bill[rate_name] = rate_set.pop()
    bill['net-gbp'] = sum_msp_kwh * 0.1
    bill['sum-msp-kwh'] = sum_msp_kwh
""",
            'properties': "{}", },
        'regexes': [
            r"/reports/77/output/\?supplier_contract_id=63", ],
        'status_code': 303, },

    # Add new era
    {
        'path': '/chellow/reports/305/output/',
        'method': 'post',
        'data': {
            'supply_id': "10",
            'start_year': "2010",
            'start_month': "01",
            'start_day': "01",
            'start_hour': "00",
            'start_minute': "00",
            'insert_era': "Insert", },
        'regexes': [
            r"/reports/7/output/\?supply_id=10", ],
        'status_code': 303, },

    # Change to new supplier contract. Supply 10
    {
        'path': '/chellow/reports/307/output/',
        'method': 'post',
        'data': {
            'era_id': "17",
            'start_year': "2010",
            'start_month': "01",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00",
            'is_ended': "false",
            'mop_contract_id': "57",
            'mop_account': "mc-22 1065 3921 534",
            'hhdc_contract_id': "53",
            'hhdc_account': "dc-22 1065 3921 534",
            'msn': "I02D89150",
            'pc_id': "3",
            'mtc_code': "801",
            'cop_id': "6",
            'ssc_code': "0393",
            'imp_llfc_code': "110",
            'imp_mpan_core': "22 1065 3921 534",
            'imp_sc': "30",
            'imp_supplier_contract_id': "63",
            'imp_supplier_account': "SA342376000", },
        'status_code': 303, },

    # Create a new batch
    {
        'path': '/chellow/reports/287/output/',
        'method': 'post',
        'data': {
            'supplier_contract_id': "63",
            'reference': "07-008",
            'description': "SSE batch", },
        'status_code': 303, },

    # Supplier contract 63.
    {
        'path': '/chellow/reports/321/output/',
        'method': 'post',
        'data': {
            'supplier_batch_id': "5", },
        'files': {'import_file': 'bills.sse.edi'},
        'status_code': 303,
        'regexes': [
            r"/reports/323/output/\?importer_id=3", ], },

    # Supplier contract 60.
    {
        'path': '/chellow/reports/323/output/?importer_id=3',
        'tries': {'max': 10, 'period': 1},
        'regexes': [
            r"<th>Reference</th>\s*<th>Account</th>\s*<th>Bill Type</th>\s*"
            "<th>MPANs</th>\s*<th>Issue Date</th>\s*<th>Start Date</th>\s*"
            "<th>Finish Date</th>\s*<th>kWh</th>\s*<th>Net</th>\s*"
            "<th>VAT</th>\s*<th>Gross</th>\s*<th>R1 MPAN</th>\s*"
            "<th>R1 Meter Serial Number</th>\s*<th>R1 Coefficient</th>\s*"
            "<th>R1 Units</th>\s*<th>R1 TPR</th>\s*"
            "<th>R1 Previous Read Date</th>\s*"
            "<th>R1 Previous Read Value</th>\s*"
            "<th>R1 Previous Read Type</th>\s*<th>R1 Present Read Date</th>\s*"
            "<th>R1 Present Read Value</th>\s*<th>R1 Present Read Type</th>\s*"
            "<th>Breakdown</th>",
            r"<td>3423760005</td>\s*<td>SA342376000</td>\s*<td>N</td>\s*"
            "<td>\[u?&#39;03 801 110 22 10653921534&#39;\]</td>\s*"
            "<td>2010-05-12 00:00</td>\s*<td>2010-01-19 00:00</td>\s*"
            "<td>2010-04-20 23:30</td>\s*<td>253</td>\s*<td>36.16</td>\s*"
            "<td>1.8</td>\s*<td>0</td>\s*"
            "<td>03 801 110 22 1065 3921 534</td>\s*<td>K87D74429</td>\s*"
            "<td>1</td>\s*<td>kWh</td>\s*<td>00001</td>\s*"
            "<td>2010-01-18 23:30</td>\s*<td>16963</td>\s*<td>E</td>\s*"
            "<td>2010-04-20 23:30</td>\s*<td>17216</td>\s*<td>E</td>",
            r"All the bills have been successfully loaded and attached to the "
            "batch\."],

        'status_code': 200},
    # Test the supplier batch checking
    {
        'path': '/chellow/reports/111/output/?batch_id=5',
        'tries': {'max': 10, 'period': 1},
        'regexes': [
            r"batch,bill-reference,bill-type,bill-kwh,bill-net-gbp,"
            "bill-vat-gbp, bill-start-date,bill-finish-date,bill-mpan-core,"
            "site-code,site-name,covered-from,covered-to,covered-bills,"
            "covered-net-gbp,virtual-net-gbp,difference-net-gbp",
            r'"07-008","3423760005","N","253","36.16","1.8",'
            '"2010-01-19 00:00","2010-04-20 23:30","22 1065 3921 534","CI017",'
            '"Roselands","2010-01-19 00:00","2010-04-20 23:30","10","36.16",'
            '"25.3","10.86","253.0","253.0","",""', ],
        'status_code': 200, },

    # Create a new site },
    {
        'name': "Test reports for a supply-less site",
        'path': '/chellow/reports/297/output/',
        'method': 'post',
        'data': {
            'code': "B00LG",
            'name': "Bieling", },
        'status_code': 303, },
    {
        'path': '/chellow/reports/13/output/?site_id=8&finish_year=2008&'
        'finish_month=07',
        'status_code': 200, },
    {
        'name': "Check can import channel snag ignores okay.",
        'path': '/chellow/reports/293/output/',
        'method': 'post',
        'files': {'import_file': 'channel-snag-ignores.csv'},
        'status_code': 303,
        'regexes': [
            r"/chellow/reports/295/output/\?process_id=13", ], },
    {
        'path': '/chellow/reports/295/output/?process_id=13',
        'tries': {'max': 10, 'period': 1},

        # Check it's loaded ok
        'regexes': [
            r"The file has been imported successfully", ],
        'status_code': 200, },
    {
        'name': "Check can import site snag ignores okay.",
        'path': '/chellow/reports/293/output/',
        'method': 'post',
        'files': {'import_file': 'site-snag-ignores.csv'},
        'status_code': 303,
        'regexes': [
            r"/reports/295/output/\?process_id=14", ], },
    {
        'path': '/chellow/reports/295/output/?process_id=14',
        'tries': {'max': 10, 'period': 1},

        # Check it's loaded ok
        'regexes': [
            r"The file has been imported successfully", ],
        'status_code': 200, },

    # Test that generator is set to None if source is 'net'. },
    {
        'name': "Create a supply, and then delete it.",
        'path': '/chellow/reports/311/output/',
        'method': 'post',
        'data': {
            'site_id': "7",
            'source_id': "1",
            'generator_type_id': "1",
            'name': "Supply H8",
            'start_year': "2010",
            'start_month': "05",
            'start_day': "26",
            'start_hour': "05",
            'start_minute': "26",
            'msn': "",
            'gsp_group_id': "3",
            'mop_contract_id': "57",
            'mop_account': "mc-22 9879 0084 358",
            'hhdc_contract_id': "53",
            'hhdc_account': "dc-22 9879 0084 358",
            'pc_id': "9",
            'mtc_code': "845",
            'cop_id': "5",
            'ssc_code': "",
            'imp_mpan_core': "22 9879 0084 358",
            'imp_llfc_code': "540",
            'imp_sc': "700",
            'imp_supplier_contract_id': "55",
            'imp_supplier_account': "d",
            'insert': "Insert", },
        'regexes': [
            r"/reports/7/output/\?supply_id=13", ],
        'status_code': 303, },

    # Check that the generator type 'chp' has been ignored.
    {
        'path': '/chellow/reports/5/output/?site_id=7',
        'regexes': [
            r"<td>net</td>\s*<td>\s*</td>", ],
        'status_code': 200, },
    {
        'path': '/chellow/reports/305/output/',
        'method': 'post',
        'data': {
            'supply_id': "13",
            'delete': "Delete", },
        'status_code': 303, },

    # Create a new batch. },
    {
        'name': "GDF CSV Bills",
        'path': '/chellow/reports/287/output/',
        'method': 'post',
        'data': {
            'supplier_contract_id': "55",
            'reference': "008",
            'description': "GDF CSV batch", },
        'status_code': 303, },

    # Supplier contract 53
    {
        'path': '/chellow/reports/321/output/',
        'method': 'post',
        'data': {
            'supplier_batch_id': "6", },

        # File has a character outside 8 bits to check unicode handling
        'files': {'import_file': 'bills.gdf.csv'},
        'status_code': 303,
        'regexes': [
            r"/reports/323/output/\?importer_id=4", ], },

    # Supplier contract 54, batch 6
    {
        'path': '/chellow/reports/323/output/?importer_id=4',
        'tries': {'max': 10, 'period': 1},
        'regexes': [
            r"<th>Reference</th>\s*<th>Account</th>\s*<th>Bill Type</th>\s*"
            "<th>MPANs</th>\s*<th>Issue Date</th>\s*<th>Start Date</th>\s*"
            "<th>Finish Date</th>\s*<th>kWh</th>\s*<th>Net</th>\s*"
            "<th>VAT</th>\s*<th>Gross</th>\s*<th>Breakdown</th>",
            r"<td>KUH773</td>\s*<td>02</td>\s*<td>N</td>\s*<td>\[\]</td>\s*"
            "<td>2010-06-09 00:00</td>\s*<td>2010-05-01 00:00</td>\s*"
            "<td>2010-05-31 23:30</td>\s*<td>32124.5</td>\s*"
            "<td>2219.41</td>\s*<td>388.4</td>\s*<td>2607.81</td>",
            r"All the bills have been successfully loaded and attached to "
            "the batch\.", ],
        'status_code': 200, },
    {
        'path': '/chellow/reports/323/output/?importer_id=4',
        'tries': {'max': 10, 'period': 1},
        'regexes': [
            r"<th>Reference</th>\s*<th>Account</th>\s*<th>Bill Type</th>\s*"
            "<th>MPANs</th>\s*<th>Issue Date</th>\s*<th>Start Date</th>\s*"
            "<th>Finish Date</th>\s*<th>kWh</th>\s*<th>Net</th>\s*"
            "<th>VAT</th>\s*<th>Gross</th>\s*<th>Breakdown</th>",
            r"<td>KUH773</td>\s*<td>02</td>\s*<td>N</td>\s*<td>\[\]</td>\s*"
            "<td>2010-06-09 00:00</td>\s*<td>2010-05-01 00:00</td>\s*"
            "<td>2010-05-31 23:30</td>\s*<td>32124.5</td>\s*"
            "<td>2219.41</td>\s*<td>388.4</td>\s*<td>2607.81</td>",
            r"All the bills have been successfully loaded and attached to "
            "the batch\.", ],
        'status_code': 200, },

    # Check the bill appears correctly in batch view
    {
        'path': '/chellow/reports/91/output/?supplier_batch_id=6',
        'regexes': [
            r"<td>2010-06-09 00:00</td>\s*<td>2010-05-01 00:00</td>\s*"
            "<td>2010-05-31 23:30</td>\s*<td>32124.5</td>\s*"
            "<td>2219.41</td>\s*<td>388.4</td>\s*<td>2607.81</td>", ],
        'status_code': 200, },
    {
        'name': "Test displaced virtual bill.",
        'path': '/chellow/reports/389/output/?site_id=1&months=1&'
        'finish_year=2010&finish_month=06',
        'tries': {'max': 10, 'period': 1},
        'regexes': [
            r"Site Code,Site Name,Associated Site Ids,From,To,Gen Types,"
            "CHP kWh,LM kWh,Turbine kWh,PV kWh,net-gbp,bsuos-kwh,bsuos-rate,"
            "bsuos-gbp,ccl-kwh,ccl-rate,ccl-gbp,ssp-rate,tlm,duos-green-kwh,"
            "duos-green-rate,duos-green-gbp,duos-reactive-gbp,"
            "duos-reactive-working,duos-standing-gbp,night-gbp,night-gsp-kwh,"
            "night-msp-kwh,other-gbp,other-gsp-kwh,other-msp-kwh,"
            "summer-pk-gbp,summer-pk-gsp-kwh,summer-pk-msp-kwh,triad-gbp,"
            "triad-working,winter-low-pk-gbp,winter-low-pk-gsp-kwh,"
            "winter-low-pk-msp-kwh,winter-off-pk-gbp,winter-off-pk-gsp-kwh,"
            "winter-off-pk-msp-kwh,winter-pk-gbp,winter-pk-gsp-kwh,"
            "winter-pk-msp-kwh,triad-actual-1-date,triad-actual-1-msp-kw,"
            "triad-actual-1-status,triad-actual-1-laf,triad-actual-1-gsp-kw,"
            "triad-actual-2-date,triad-actual-2-msp-kw,triad-actual-2-status,"
            "triad-actual-2-laf,triad-actual-2-gsp-kw,triad-actual-3-date,"
            "triad-actual-3-msp-kw,triad-actual-3-status,triad-actual-3-laf,"
            "triad-actual-3-gsp-kw,triad-actual-gsp-kw,triad-actual-rate,"
            "triad-actual-gbp,triad-estimate-1-date,triad-estimate-1-msp-kw,"
            "triad-estimate-1-status,triad-estimate-1-laf,"
            "triad-estimate-1-gsp-kw,triad-estimate-2-date,"
            "triad-estimate-2-msp-kw,triad-estimate-2-status,"
            "triad-estimate-2-laf,triad-estimate-2-gsp-kw,"
            "triad-estimate-3-date,triad-estimate-3-msp-kw,"
            "triad-estimate-3-status,triad-estimate-3-laf,"
            "triad-estimate-3-gsp-kw,triad-estimate-gsp-kw,"
            "triad-estimate-rate,triad-estimate-months,triad-estimate-gbp,"
            "triad-all-estimates-months,triad-all-estimates-gbp,problem",
            r'"CI004","Lower Treave","","2010-06-01 00:00","2010-06-30 23:30",'
            '"chp","","","","","0.0","0.0","","0.0","","0.0047","","","","0",'
            '"0.0013","0.0","","","","0.0","0.0","0","0.0","0.0","0","0.0",'
            '"0.0","0","","","","0","0","","0","0","","0","0","","","","","",'
            '"","","","","","","","","","","","","","2010-01-07 17:00","0",'
            '"E","1.078","0.0","2010-01-25 17:00","0","E","1.078","0.0",'
            '"2009-12-15 17:00","0","E","1.078","0.0","0.0","26.057832","1",'
            '"0.0","","",""', ],
        'status_code': 200, },

    # Try a 12 month run
    {
        'path': '/chellow/reports/389/output/?site_id=1&months=12&'
        'finish_year=2011&finish_month=06',
        'status_code': 200, },
    {
        'name': "Test bulk ignore.",
        'path': '/chellow/reports/279/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "53",
            'ignore_year': "2008",
            'ignore_month': "09",
            'ignore_day': "01",
            'ignore_hour': "00",
            'ignore_minute': "00",
            'ignore_snags': "Ignore Snags", },
        'status_code': 303, },
    {
        'name': "Check that a era can be deleted. Supply 1",
        'path': '/chellow/reports/307/output/',
        'method': 'post',
        'data': {
            'era_id': "14",
            'delete': "Delete", },
        'status_code': 303, },
    {
        'name': "Check a contract virtual bill that crosses a era boundary "
        "comes out correctly.",
        'path': '/chellow/reports/291/output/?supply_id=11&start_year=2010&'
        'start_month=04&start_day=01&start_hour=00&start_minute=00&'
        'finish_year=2010&finish_month=04&finish_day=30&finish_hour=23&'
        'finish_minute=30',
        'status_code': 200,
        'regexes': [
            r'"Imp MPAN Core","Exp MPAN Core","Site Code","Site Name",'
            '"Account","From","To","","mop-net-gbp","mop-problem","",'
            '"dc-net-gbp","dc-problem","","imp-supplier-net-gbp",'
            '"imp-supplier-vat-gbp","imp-supplier-gross-gbp",'
            '"imp-supplier-sum-msp-kwh","imp-supplier-problem"',
            r'"22 9974 3438 105","","CI005","Wheal Rodney","SA341665",'
            '"2010-04-01 00:00","2010-04-13 23:30","","0","","","0","","",'
            '"0.0","0.0","0.0","0",""', ], },
    {
        'name': "NHH CSV import",
        'path': '/chellow/reports/287/output/',
        'method': 'post',
        'data': {
            'supplier_contract_id': "63",
            'reference': "07-002",
            'description': "nhh csv batch", },
        'status_code': 303, },

    # Supplier contract 63
    {
        'path': '/chellow/reports/321/output/',
        'method': 'post',
        'data': {
            'supplier_batch_id': "7", },
        'files': {'import_file': 'bills-nhh.csv'},
        'status_code': 303,
        'regexes': [
            r"/reports/323/output/\?importer_id=5", ], },

    # Supplier contract 60, batch 7
    {
        'path': '/chellow/reports/323/output/?importer_id=5',
        'tries': {'max': 10, 'period': 1},
        'status_code': 200,
        'regexes': [
            r"All the bills have been successfully loaded and attached to "
            "the batch\.", ], },

    # Supplier contract 60, batch 7, bill 10
    {
        'path': '/chellow/reports/31/output/?supplier_read_id=7',
        'regexes': [
            r'31</option>\s*</select>\s*<select name="present_hour">\s*'
            '<option value="0">00</option>\s*<option value="1">01</option>\s*'
            '<option value="2">02</option>\s*<option value="3">03</option>\s*'
            '<option value="4">04</option>\s*<option value="5">05</option>\s*'
            '<option value="6">06</option>\s*<option value="7">07</option>\s*'
            '<option value="8">08</option>\s*<option value="9">09</option>\s*'
            '<option value="10">10</option>\s*'
            '<option value="11">11</option>\s*'
            '<option value="12">12</option>\s*'
            '<option value="13">13</option>\s*'
            '<option value="14">14</option>\s*'
            '<option value="15">15</option>\s*'
            '<option value="16">16</option>\s*'
            '<option value="17">17</option>\s*'
            '<option value="18">18</option>\s*'
            '<option value="19">19</option>\s*'
            '<option value="20">20</option>\s*'
            '<option value="21">21</option>\s*'
            '<option value="22">22</option>\s*'
            '<option value="23" selected>23</option>\s*'
            '</select>:<select name="present_minute">\s*'
            '<option value="0">00</option>\s*'
            '<option value="30" selected>30</option>\s*</select>',
            r'<input type="hidden" name="supplier_read_id" value="7">', ], },
    {
        'name': "Test viewers' search",
        'path': '/chellow/reports/99/output/?search_pattern=',
        'regexes': [
            r'<td>\s*'
            '<a href="/chellow/reports/7/output/\?supply_id=9">supply</a>\s*'
            '</td>\s*<td>P96C93722</td>',
            r"<td>\s*</td>\s*<td>\s*</td>\s*<td>\s*</td>\s*<td>\s*"
            "00 845 581\s*22 0470 7514 535\s*</td>", ],
        'status_code': 200, },

    # Check that searching for an account with a space works
    {
        'path': '/chellow/reports/99/output/?search_pattern=141%205532',
        'regexes': [
            r"/chellow/reports/7/output/\?supply_id=6", ],
        'status_code': 307, },

    # Check that searching on an MSN works
    {
        'path': '/chellow/reports/99/output/?search_pattern=P96C93722',
        'regexes': [
            r"/chellow/reports/7/output/\?supply_id=9", ],
        'status_code': 307, },
    {
        'name': "Check can view a supply.",
        'path': '/chellow/reports/7/output/?supply_id=2',

        # Check there's a link to raw HH data
        'regexes': [
            r"/reports/17/output/\?",

            # Check we can see the site
            r'<a href="/chellow/reports/5/output/\?site_id=1" title="Lower '
            'Treave">CI004</a>',

            # Check a link to supplier bill is correct
            r'<a href="/chellow/reports/105/output/\?supplier_bill_id=11">'
            'View</a>',

            # Check link to supply duration is correct
            r'<form action="/chellow/reports/149/output/">\s*<fieldset>\s*'
            '<input type="hidden" name="supply_id"',
            r'<td rowspan="4">\s*'
            '<a href="/chellow/reports/55/output/\?pc_id=9" title="Half-'
            'hourly">00</a>\s*</td>\s*<td rowspan="4"></td>\s*'
            '<td rowspan="4">\s*'
            '<a href="/chellow/reports/63/output/\?mtc_id=529" title="HH '
            'COP5 And Above With Comms">845</a>\s*</td>', ],
        'status_code': 200, },

    # Supply 10 },
    {
        'name': "Check that if the end date of a era is altered, it can tell "
        "if there's a succeeding era.",
        'path': '/chellow/reports/307/output/',
        'method': 'post',
        'data': {
            'era_id': "10",
            'start_year': "2005",
            'start_month': "09",
            'start_day': "06",
            'start_hour': "00",
            'start_minute': "00",
            'is_ended': "true",
            'finish_year': "2010",
            'finish_month': "01",
            'finish_day': "03",
            'finish_hour': "23",
            'finish_minute': "30",
            'mop_contract_id': "57",
            'mop_account': "mc-22 1065 3921 534",
            'hhdc_contract_id': "54",
            'hhdc_account': "dc-22 1065 3921 534",
            'msn': "I02D89150",
            'pc_id': "3",
            'mtc_code': "801",
            'cop_id': "5",
            'ssc_code': "0393",
            'imp_llfc_code': "110",
            'imp_mpan_core': "22 1065 3921 534",
            'imp_sc': "30",
            'imp_supplier_contract_id': "59",
            'imp_supplier_account': "SA342376", },
        'status_code': 303, },
    {
        'name': "Check that it works if a supply era is inserted by CSV "
        "before the beginning of a supply ",
        'path': '/chellow/reports/293/output/',
        'method': 'post',
        'files': {'import_file': 'era-insert.csv'},
        'status_code': 303,
        'regexes': [
            r"/reports/295/output/\?process_id=15", ], },
    {
        'path': '/chellow/reports/295/output/?process_id=15',
        'tries': {'max': 10, 'period': 1},

        # Check it's loaded ok
        'regexes': [
            r"The file has been imported successfully", ],
        'status_code': 200, },

    # Supply 9
    {
        'path': '/chellow/reports/307/output/?era_id=20',

        # Check the import supplier account is there
        'regexes': [
            r"341664", ],
        'status_code': 200, },
    {
        'name': "Check that the general import of register reads works.",
        'path': '/chellow/reports/293/output/',
        'method': 'post',
        'files': {'import_file': 'bills-general.csv'},
        'status_code': 303,
        'regexes': [
            r"/reports/295/output/\?process_id=16", ], },
    {
        'path': '/chellow/reports/295/output/?process_id=16',
        'tries': {'max': 10, 'period': 1},

        # Check it's loaded ok
        'regexes': [
            r"The file has been imported successfully", ],
        'status_code': 200, },
    {
        'path': '/chellow/reports/105/output/?supplier_bill_id=14',
        'tries': {'max': 10, 'period': 1},

        # Check it's loaded ok
        'regexes': [
            r'<td>\s*<a href="/chellow/reports/111/output/\?bill_id=14">Check'
            '</a>\s*</td>',
            r'<td>38992</td>\s*<td>\s*<a title="Estimated"\s*'
            'href="/chellow/reports/143/output/\?type-id=4">E</a>\s*</td>\s*'
            '<td>2007-01-17 00:00</td>\s*<td>39000\s*</td>\s*<td>\s*'
            '<a title="Estimated"\s*'
            'href="/chellow/reports/143/output/\?type-id=4">E</a>\s*</td>', ],
        'status_code': 200, },
    {
        'name': "Check the 'update bill' page.",
        'path': '/chellow/reports/165/output/?supplier_bill_id=10',
        'status_code': 200,
        'regexes': [
            r"type_id",
            r'<option value="2" selected>N Normal</option>',
            r'name="account" value="SA342376000"', ], },
    {
        'name': "Check the batch page.",
        'path': '/chellow/reports/91/output/?supplier_batch_id=5',
        'status_code': 200,
        'regexes': [
            r"<td>2010-01-19 00:00</td>\s*<td>2010-04-20 23:30</td>", ], },
    {
        'name': "Test supply era update for a supply with 2 mpans.",
        'path': '/chellow/reports/293/output/',
        'method': 'post',
        'files': {'import_file': 'era-update-2-mpans.csv'},
        'status_code': 303,
        'regexes': [
            r"/reports/295/output/\?process_id=17", ], },
    {
        'path': '/chellow/reports/295/output/?process_id=17',
        'tries': {'max': 10, 'period': 1},

        # Check it's loaded ok
        'regexes': [
            r"The file has been imported successfully", ],
        'status_code': 200, },

    # Insert a new batch },
    {
        'name': "Add batch to HHDC contract",
        'path': '/chellow/reports/281/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "53",
            'reference': "001-7t",
            'description': "hhdc batch", },
        'status_code': 303,
        'regexes': [
            r"/reports/203/output/\?hhdc_batch_id=8", ], },

    # Check that it's there to edit. HHDC contract 53
    {
        'path': '/chellow/reports/283/output/?hhdc_batch_id=8',
        'status_code': 200, },

    # Contract 52 },
    {
        'name': "Try adding bills to the HHDC batch",
        'path': '/chellow/reports/327/output/?hhdc_batch_id=8',
        'method': 'post',
        'data': {
            'hhdc_batch_id': "8", },
        'files': {'import_file': 'hhdc-bill.csv'},
        'status_code': 303,
        'regexes': [
            r"/reports/329/output/\?importer_id=6", ], },

    # Contract 52 batch 8
    {
        'path': '/chellow/reports/329/output/?importer_id=6',
        'tries': {'max': 10, 'period': 1},
        'status_code': 200,
        'regexes': [
            r"All the bills have been successfully loaded and attached to "
            "the batch\.", ], },

    # Insert a new batch. },
    {
        'name': "Add batch to MOP contract",
        'path': '/chellow/reports/353/output/',
        'method': 'post',
        'data': {
            'mop_contract_id': "57",
            'reference': "99/992",
            'description': "mop batch", },
        'status_code': 303,
        'regexes': [
            r"/reports/193/output/\?mop_batch_id=9", ], },

    # Check that it's there in edit mode. Contract 57
    {
        'path': '/chellow/reports/355/output/?mop_batch_id=9',
        'status_code': 200,
        'regexes': [
            r'<input type="hidden" name="mop_batch_id" value="9">', ], },

    # Check confirm-delete page. Contract 57
    {
        'path': '/chellow/reports/355/output/?mop_batch_id=9&'
        'confirm_delete=Delete',
        'status_code': 200,
        'regexes': [
            r'<input type="hidden" name="mop_batch_id" value="9">', ], },

    # Check we can see it in 'view' mode. Contract 55
    {
        'path': '/chellow/reports/193/output/?mop_batch_id=9',
        'status_code': 200, },

    # Mop contract 54 },
    {
        'name': "Try adding bills to the MOP batch",
        'path': '/chellow/reports/331/output/',
        'method': 'post',
        'data': {
            'mop_batch_id': "9", },
        'files': {'import_file': 'mop-bill.csv'},
        'status_code': 303,
        'regexes': [
            r"/reports/333/output/\?importer_id=7", ], },

    # Mop contract 54, batch 9
    {
        'path': '/chellow/reports/333/output/?importer_id=7',
        'tries': {'max': 10, 'period': 1},
        'status_code': 200,
        'regexes': [
            r"All the bills have been successfully loaded and attached to "
            "the batch\.", ], },
    {
        'name': "If a new supply has a blank LLFC field, check it gives a "
        "good error message.",
        'path': '/chellow/reports/311/output/',
        'method': 'post',
        'data': {
            'site_id': "7",
            'source_id': "1",
            'name': "Supply 54",
            'start_year': "2010",
            'start_month': "05",
            'start_day': "26",
            'start_hour': "00",
            'start_minute': "00",
            'msn': "",
            'gsp_group_id': "3",
            'mop_contract_id': "57",
            'mop_account': "mc-22 9879 0084 358",
            'hhdc_contract_id': "53",
            'hhdc_account': "dc-22 9879 0084 358",
            'pc_id': "9",
            'mtc_code': "845",
            'cop_id': "5",
            'ssc_code': "",
            'imp_mpan_core': "22 9879 0084 358",
            'imp_llfc_code': "",
            'imp_sc': "700",
            'imp_supplier_contract_id': "55",
            'imp_supplier_account': "d",
            'insert': "Insert", },
        'regexes': [
            r"There is no LLFC with the code &#39;&#39; associated with the "
            "DNO 22\.", ],
        'status_code': 400, },
    {
        'name': "If a new supply has a blank import sc field, check it gives "
        "a good error message.",
        'path': '/chellow/reports/311/output/',
        'method': 'post',
        'data': {
            'site_id': "7",
            'source_id': "1",
            'name': "Supply 54",
            'start_year': "2010",
            'start_month': "05",
            'start_day': "26",
            'start_hour': "00",
            'start_minute': "00",
            'msn': "",
            'gsp_group_id': "3",
            'mop_contract_id': "57",
            'mop_account': "mc-22 9879 0084 358",
            'hhdc_contract_id': "53",
            'hhdc_account': "dc-22 9879 0084 358",
            'pc_id': "9",
            'mtc_code': "845",
            'cop_id': "5",
            'ssc_code': "",
            'imp_mpan_core': "22 9879 0084 358",
            'imp_llfc_code': "570",
            'imp_sc': "",
            'imp_supplier_contract_id': "55",
            'imp_supplier_account': "d",
            'insert': "Insert", },
        'regexes': [
            r"Problem parsing the field imp_sc as an integer: invalid literal "
            "for int\(\) with base 10: ", ],
        'status_code': 400, },
    {
        'name': "If a new supply has a blank MTC code field, check it gives "
        "a good error message.",
        'path': '/chellow/reports/311/output/',
        'method': 'post',
        'data': {
            'site_id': "7",
            'source_id': "1",
            'name': "Supply 54",
            'start_year': "2010",
            'start_month': "05",
            'start_day': "26",
            'start_hour': "00",
            'start_minute': "00",
            'msn': "",
            'gsp_group_id': "3",
            'mop_contract_id': "57",
            'mop_account': "mc-22 9879 0084 358",
            'hhdc_contract_id': "53",
            'hhdc_account': "dc-22 9879 0084 358",
            'pc_id': "9",
            'mtc_code': "",
            'cop_id': "5",
            'ssc_code': "",
            'imp_mpan_core': "22 9879 0084 358",
            'imp_llfc_code': "570",
            'imp_sc': "700",
            'imp_supplier_contract_id': "55",
            'imp_supplier_account': "d",
            'insert': "Insert", },
        'regexes': [
            r"The MTC code must be a whole number\.", ],
        'status_code': 400, },
    {
        'name': "Try view page of meter payment types.",
        'path': '/chellow/reports/133/output/',
        'status_code': 200, },
    {
        'name': "Try a monthly sites duration for a site with a 3rd party "
        "supply.",
        'path': '/chellow/reports/311/output/',
        'method': 'post',
        'data': {
            'site_id': "4",
            'source_id': "5",
            'name': "3",
            'start_year': "2010",
            'start_month': "05",
            'start_day': "26",
            'start_hour': "00",
            'start_minute': "00",
            'msn': "",
            'gsp_group_id': "3",
            'mop_contract_id': "57",
            'mop_account': "mc-22 9789 0534 938",
            'hhdc_contract_id': "53",
            'hhdc_account': "dc-22 9789 0534 938",
            'pc_id': "3",
            'mtc_code': "801",
            'cop_id': "5",
            'ssc_code': "393",
            'imp_mpan_core': "22 9789 0534 938",
            'imp_llfc_code': "110",
            'imp_sc': "0",
            'imp_supplier_contract_id': "63",
            'imp_supplier_account': "taa2",
            'insert': "Insert", },
        'regexes': [
            r"/chellow/reports/7/output/\?supply_id=16", ],
        'status_code': 303, },
    {
        'path': '/chellow/reports/161/output/?site_id=4&months=1&'
        'finish_year=2010&finish_month=07',
        'status_code': 303, },
    {
        'path': '/chellow/reports/251/output/',
        'tries': {'max': 20, 'period': 1},
        'regexes': [
            r"FINISHED_site_monthly_duration_for_CI017_1_to_2010_7.csv", ],
        'status_code': 200, },
    {
        'path': '/chellow/reports/253/output/?'
        'name=FINISHED_site_monthly_duration_for_CI017_1_to_2010_7.csv',
        'regexes': [
            r'"CI017","Roselands","","3rd-party,net","","2010-07-31 23:30",'
            '"0","0","0","0","0","0","0","0","1593.3414","0","0","1593.3414"'
            ',"0.0","0","0","hh",""', ],
        'status_code': 200, },
    {
        'name': "Try creating and deleting a rate script for a non-core "
        "contract (templater).",
        'path': '/chellow/reports/275/output/',
        'method': 'post',
        'data': {
            'non_core_contract_id': "31",
            'start_year': "2010",
            'start_month': "04",
            'start_day': "01",
            'start_hour': "00",
            'start_minute': "00",
            'insert': "Insert", },
        'regexes': [
            r"/chellow/reports/271/output/\?rate_script_id=318", ],
        'status_code': 303, },
    {
        'path': '/chellow/reports/273/output/?rate_script_id=318&'
        'delete=Delete',
        'regexes': [
            r"Are you sure you want to delete this rate script\?", ],
        'status_code': 200, },
    {
        'path': '/chellow/reports/273/output/',
        'method': 'post',
        'data': {
            'rate_script_id': "318",
            'delete': "Delete", },
        'status_code': 303, },
    {
        'path': '/chellow/reports/271/output/?rate_script_id=318',
        'status_code': 404, },
    {
        'name': "Try adding a rate script before other rate scripts.",
        'path': '/chellow/reports/275/output/',
        'method': 'post',
        'data': {
            'non_core_contract_id': "31",

            # Templater
            'start_year': "1999",
            'start_month': "04",
            'start_day': "01",
            'start_hour': "00",
            'start_minute': "00",
            'insert': "Insert", },
        'regexes': [
            r"/chellow/reports/271/output/\?rate_script_id=319", ],
        'status_code': 303, },
    {
        'path': '/chellow/reports/273/output/?rate_script_id=319',
        'regexes': [
            r'<input name="finish_year" maxlength="4" size="4" value="2010">',

            # Check that the start hour of a non-core rate script is correct."
            r'<select name="start_hour">\s*'
            '<option value="0" selected>00</option>', ],
        'status_code': 200, },
    {
        'path': '/chellow/reports/273/output/',
        'method': 'post',
        'data': {
            'rate_script_id': "319",
            'delete': "Delete", },
        'status_code': 303, },

    # Supplier contract 54 },
    {
        'name': "Adding a bill manually.",
        'path': '/chellow/reports/313/output/',
        'method': 'post',
        'data': {
            'supplier_batch_id': "6",
            'mpan_core': "22 9813 2107 763",
            'reference': "KUH774",
            'issue_year': "2010",
            'issue_month': "12",
            'issue_day': "06",
            'issue_hour': "00",
            'issue_minute': "00",
            'start_year': "2010",
            'start_month': "12",
            'start_day': "06",
            'start_hour': "00",
            'start_minute': "00",
            'finish_year': "2010",
            'finish_month': "12",
            'finish_day': "06",
            'finish_hour': "00",
            'finish_minute': "00",
            'kwh': "0",
            'net': "0",
            'vat': "0",
            'gross': "0",
            'account': "02",
            'bill_type_id': "1",
            'breakdown': "{}", },
        'regexes': [
            r"/chellow/reports/105/output/\?supplier_bill_id=18", ],
        'status_code': 303, },

    # Supplier contract 52, batch 6
    {
        'path': '/chellow/reports/165/output/?supplier_bill_id=18',
        'regexes': [
            r'<select name="start_day">\s*<option value="1">01</option>\s*'
            '<option value="2">02</option>\s*<option value="3">03</option>\s*'
            '<option value="4">04</option>\s*<option value="5">05</option>\s*'
            '<option value="6" selected>06</option>\s*'
            '<option value="7">07</option>\s*<option value="8">08</option>\s*'
            '<option value="9">09</option>\s*<option value="10">10</option>\s*'
            '<option value="11">11</option>\s*'
            '<option value="12">12</option>\s*'
            '<option value="13">13</option>\s*'
            '<option value="14">14</option>\s*'
            '<option value="15">15</option>\s*'
            '<option value="16">16</option>\s*'
            '<option value="17">17</option>\s*'
            '<option value="18">18</option>\s*'
            '<option value="19">19</option>\s*'
            '<option value="20">20</option>\s*'
            '<option value="21">21</option>\s*'
            '<option value="22">22</option>\s*'
            '<option value="23">23</option>\s*'
            '<option value="24">24</option>\s*'
            '<option value="25">25</option>\s*'
            '<option value="26">26</option>\s*'
            '<option value="27">27</option>\s*'
            '<option value="28">28</option>\s*'
            '<option value="29">29</option>\s*'
            '<option value="30">30</option>\s*'
            '<option value="31">31</option>\s*'
            '</select>\s*<select name="start_hour">\s*'
            '<option value="0" selected>00</option>\s*'
            '<option value="1">01</option>\s*<option value="2">02</option>\s*'
            '<option value="3">03</option>\s*<option value="4">04</option>\s*'
            '<option value="5">05</option>\s*<option value="6">06</option>\s*'
            '<option value="7">07</option>\s*<option value="8">08</option>\s*'
            '<option value="9">09</option>\s*<option value="10">10</option>\s*'
            '<option value="11">11</option>\s*'
            '<option value="12">12</option>\s*'
            '<option value="13">13</option>\s*'
            '<option value="14">14</option>\s*'
            '<option value="15">15</option>\s*'
            '<option value="16">16</option>\s*'
            '<option value="17">17</option>\s*'
            '<option value="18">18</option>\s*'
            '<option value="19">19</option>\s*'
            '<option value="20">20</option>\s*'
            '<option value="21">21</option>\s*'
            '<option value="22">22</option>\s*'
            '<option value="23">23</option>\s*'
            '</select>:<select name="start_minute">\s*'
            '<option value="0" selected>00</option>\s*'
            '<option value="30">30</option>\s*</select>',
            r'<select name="finish_day">\s*<option value="1">01</option>\s*'
            '<option value="2">02</option>\s*<option value="3">03</option>\s*'
            '<option value="4">04</option>\s*<option value="5">05</option>\s*'
            '<option value="6" selected>06</option>\s*'
            '<option value="7">07</option>\s*<option value="8">08</option>\s*'
            '<option value="9">09</option>\s*<option value="10">10</option>\s*'
            '<option value="11">11</option>\s*'
            '<option value="12">12</option>\s*'
            '<option value="13">13</option>\s*'
            '<option value="14">14</option>\s*'
            '<option value="15">15</option>\s*'
            '<option value="16">16</option>\s*'
            '<option value="17">17</option>\s*'
            '<option value="18">18</option>\s*'
            '<option value="19">19</option>\s*'
            '<option value="20">20</option>\s*'
            '<option value="21">21</option>\s*'
            '<option value="22">22</option>\s*'
            '<option value="23">23</option>\s*'
            '<option value="24">24</option>\s*'
            '<option value="25">25</option>\s*'
            '<option value="26">26</option>\s*'
            '<option value="27">27</option>\s*'
            '<option value="28">28</option>\s*'
            '<option value="29">29</option>\s*'
            '<option value="30">30</option>\s*'
            '<option value="31">31</option>\s*'
            '</select>\s*<select name="finish_hour">\s*'
            '<option value="0" selected>00</option>\s*'
            '<option value="1">01</option>\s*<option value="2">02</option>\s*'
            '<option value="3">03</option>\s*<option value="4">04</option>\s*'
            '<option value="5">05</option>\s*<option value="6">06</option>\s*'
            '<option value="7">07</option>\s*<option value="8">08</option>\s*'
            '<option value="9">09</option>\s*<option value="10">10</option>\s*'
            '<option value="11">11</option>\s*'
            '<option value="12">12</option>\s*'
            '<option value="13">13</option>\s*'
            '<option value="14">14</option>\s*'
            '<option value="15">15</option>\s*'
            '<option value="16">16</option>\s*'
            '<option value="17">17</option>\s*'
            '<option value="18">18</option>\s*'
            '<option value="19">19</option>\s*'
            '<option value="20">20</option>\s*'
            '<option value="21">21</option>\s*'
            '<option value="22">22</option>\s*'
            '<option value="23">23</option>\s*'
            '</select>:<select name="finish_minute">\s*'
            '<option value="0" selected>00</option>\s*'
            '<option value="30">30</option>\s*</select>', ],
        'status_code': 200, },
    {
        'name': "Check that bill with two sets of register reads gets "
        "displayed correctly.",
        'path': '/chellow/reports/7/output/?supply_id=10',
        'regexes': [
            r'<td rowspan="2">\s*'
            '<a href="/chellow/reports/201/output/\?bill_type_id=2" '
            'title="Normal">N</a>\s*</td>\s*'
            '<td style="border-right: none;">\s*'
            '<a title="2011-02-04 23:30 I02D89150">34285</a>\s*</td>',
            r'25927</a>\s*</td>\s*'
            '<td style="border-left: none; text-align: right;">\s*E\s*</td>\s*'
            '<td>\s*</td>\s*<td style="border-right: none;">\s*</td>\s*'
            '<td style="border-left: none; text-align: right;">\s*</td>\s*'
            '<td style="border-right: none;">\s*</td>\s*'
            '<td style="border-left: none; text-align: right;">\s*</td>\s*'
            '</tr>',

            # Check form action for virtual bills is correct
            r'<form action="/chellow/reports/291/output/">',

            # Check link to TPR from outer read
            r'<td>\s*'
            '<a href="/chellow/reports/97/output/\?tpr_id=2">00003</a>\s*'
            '</td>', ],
        'status_code': 200, },

    # Supplier contract 61 },
    {
        'name': "Deleting a batch with bills with register reads.",
        'path': '/chellow/reports/289/output/',
        'method': 'post',
        'data': {
            'supplier_batch_id': "5",
            'delete': "Delete", },
        'status_code': 303, },
    {
        'name': "Check 'insert supplier batch' page.",
        'path': '/chellow/reports/287/output/?supplier_contract_id=63',
        'regexes': [
            r'="description"', ], },
    {
        'name': "Viewing the insert batch page of a DC contract.",
        'path': '/chellow/reports/281/output/?hhdc_contract_id=53',
        'regexes': [
            r'="description"', ], },
    {
        'name': "Viewing a batch in view mode, when it has a custom report.",
        'path': '/chellow/reports/269/output/',
        'method': 'post',
        'data': {
            'non_core_contract_id': "13",
            'name': "configuration",
            'charge_script': "",
            'properties': """
{
    'ips': {'127.0.0.1': 'implicit-user@localhost'},
    'site_links': [
        {'name': 'Google Maps', 'href': 'https://maps.google.com/maps?q='}],
    'batch_reports': [2]}
""", },
        'status_code': 303, },

    # Check that we can see a MOP batch okay. Contract 56
    {
        'path': '/chellow/reports/193/output/?mop_batch_id=9',
        'regexes': [
            r"/reports/2/output/", ],
        'status_code': 200, },

    # Check that we can see a supplier batch okay. Contract 55
    {
        'path': '/chellow/reports/91/output/?supplier_batch_id=4',
        'regexes': [
            r"/reports/2/output/", ],
        'status_code': 200, },
    {
        'name': "Check 'no channel' error when importing hh data.",
        'path': '/chellow/reports/211/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "53", },
        'files': {'import_file': 'hh-no-channel.simple.csv'},
        'status_code': 303,
        'regexes': [
            r"/reports/65/output/\?hhdc_contract_id=53&process_id=13", ], },
    {
        'path': '/chellow/reports/65/output/?hhdc_contract_id=53&'
        'process_id=13',
        'tries': {'max': 10, 'period': 1},
        'regexes': [
            r"There is no channel for the datum: \{&#39;channel_type&#39;: "
            "&#39;REACTIVE_EXP&#39;, &#39;mpan_core&#39;: &#39;22 4862 4512 "
            "332&#39;, &#39;start_date&#39;: "
            "datetime.datetime\(2010, 2, 4, 20, 0, tzinfo=&lt;UTC&gt;\), "
            "&#39;status&#39;: &#39;A&#39;, &#39;value&#39;: "
            "Decimal\(&#3\d;30.4339&#3\d;\)\}\.", ],
        'status_code': 200, },
    {
        'name': "Check the bill import page.",
        'path': '/chellow/reports/211/output/?hhdc_contract_id=53',
        'status_code': 200,
        'regexes': [
            r"/reports/115/output/\?hhdc_contract_id=53", ], },

    # Can we add a new era ok? },
    {
        'name': "Check good error message if new era has same start date as "
        "existing era.",
        'path': '/chellow/reports/305/output/',
        'method': 'post',
        'data': {
            'supply_id': "10",
            'start_year': "2005",
            'start_month': "09",
            'start_day': "06",
            'start_hour': "00",
            'start_minute': "00",
            'insert_era': "Insert", },
        'regexes': [
            r"There&#39;s already an era with that start date\.", ],
        'status_code': 400, },
    {
        'name': "Check MOP and DC bills are displaying correctly",
        'path': '/chellow/reports/7/output/?supply_id=5',
        'regexes': [
            r'<td>\s*'
            '<a href="/chellow/reports/203/output/\?hhdc_batch_id=8">001-7t'
            '</a>\s*</td>\s*<td>00031</td>\s*<td>22 0883 6932 301</td>\s*'
            '<td>2007-09-01 00:00</td>',
            r'<td>\s*'
            '<a href="/chellow/reports/193/output/\?mop_batch_id=9">99/992'
            '</a>\s*</td>\s*<td>06</td>\s*<td>22 0883 6932 301</td>',

            # Check that MOP bill before supply start is displayed
            r'<td>\s*'
            '<a href="/chellow/reports/193/output/\?mop_batch_id=9">99/992'
            '</a>\s*</td>\s*<td>08</td>\s*<td>22 0883 6932 301</td>',

            # Check that channel type is displayed
            r'<tr>\s*<td>\s*'
            '<a href="/chellow/reports/301/output/\?channel_id=16">'
            'ACTIVE</a>\s*'
            '<a href="/chellow/reports/301/output/\?channel_id=17">'
            'REACTIVE_IMP</a>\s*</td>', ],
        'status_code': 200, },
    {
        'name': "View the note editing page.",
        'path': '/chellow/reports/239/output/?supply_id=2',
        'status_code': 200, },
    {
        'name': "Try editing a note.",
        'path': '/chellow/reports/239/output/',
        'method': 'post',
        'data': {
            'supply_id': "2",
            'is_important': "True",
            'category': "general",
            'body': "", },
        'status_code': 303, },

    # Try importing HH data from FTP server.
    {
        'name': "Update Contract",
        'path': '/chellow/reports/279/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "53",
            'party_id': "97",  # DASL
            'name': "HH contract",
            'charge_script': """
def virtual_bill_titles():
    return ['net-gbp', 'problem']

def virtual_bill(supply_source):
    supply_source.dc_bill['net-gbp'] = 0
""",
            'properties': """
{'has_importer': True,
'file_type': '.df2',
'hostname': 'localhost',
'port': 2121,
'username': 'chellow',
'password': 'HixaNfUBOf*u',
'directories': ['.']}
""", },
        'status_code': 303, },

    # Do an 'import now'
    {
        'path': '/chellow/reports/213/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "53", },
        'status_code': 303, },
    {
        'path': '/chellow/reports/213/output/?hhdc_contract_id=53',
        'tries': {'max': 10, 'period': 1},
        'regexes': [
            r"File downloaded successfully\.", ], },
    {
        'path': '/chellow/reports/115/output/?hhdc_contract_id=53',
        'regexes': [
            r"hh_data\.df2", ], },
    {
        'name': "Try startup and shutdown.",
        'path': '/chellow/reports/171/output/',
        'method': 'post',
        'tries': {'max': 10, 'period': 1},
        'data': {
            'run_shutdown': "Shutdown", },
        'regexes': [
            r"Shut down successfully.", ], },
    {
        'path': '/chellow/reports/171/output/',
        'method': 'post',
        'data': {
            'run_startup': "Run", }, },
    {
        'name': "Check that later bills are at the top.",
        'path': '/chellow/reports/7/output/?supply_id=1',
        'regexes': [
            r"supplier_bill_id=7.*supplier_bill_id=1",
            r"2007-02-28 23:30", ],
        'status_code': 200, },

    # Change generation to NHH. Supply 7 },
    {
        'name': "Check that CRC report works for an AMR with no data.",
        'path': '/chellow/reports/307/output/',
        'method': 'post',
        'data': {
            'era_id': "7",
            'msn': "",
            'start_year': "2003",
            'start_month': "08",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00",
            'is_ended': "false",
            'pc_id': "4",
            'mtc_code': "845",
            'cop_id': "5",
            'ssc_code': "393",
            'mop_contract_id': "57",
            'mop_account': "mc-22 6354 2983 570",
            'hhdc_contract_id': "53",
            'hhdc_account': "01",
            'imp_llfc_code': "210",
            'imp_mpan_core': "22 4862 4512 332",
            'imp_sc': "230",
            'imp_supplier_contract_id': "59",
            'imp_supplier_account': "141 5532", },
        'status_code': 303, },

    # Run CRC report for month without data
    {
        'path': '/chellow/reports/207/output/?supply_id=7&year=2012',
        'regexes': [
            r'"7","22 4862 4512 332"', ],
        'status_code': 200, },

    # Supply 9 },
    {
        'name': "Test monthly supplies duration for an unmetered supply.",
        'path': '/chellow/reports/307/output/',
        'method': 'post',
        'data': {
            'era_id': "20",
            'start_year': "2010",
            'start_month': "10",
            'start_day': "11",
            'start_hour': "00",
            'start_minute': "00",
            'is_ended': "false",
            'mop_contract_id': "57",
            'mop_account': "mc-22 0195 4836 192",
            'hhdc_contract_id': "54",
            'hhdc_account': "dc-22 0195 4836 192",
            'msn': "P96C93722",
            'pc_id': "8",
            'mtc_code': "857",
            'cop_id': "8",
            'ssc_code': "0428",
            'imp_llfc_code': "980",
            'imp_mpan_core': "22 0195 4836 192",
            'imp_sc': "304",
            'imp_supplier_contract_id': "59",
            'imp_supplier_account': "SA342376", },
        'status_code': 303, },
    {
        'path': '/chellow/reports/291/output/?supply_id=9&start_year=2011&'
        'start_month=05&start_day=01&start_hour=00&start_minute=0&'
        'finish_year=2011&finish_month=05&finish_day=31&finish_hour=23&'
        'finish_minute=30',
        'regexes': [
            r'"Imp MPAN Core","Exp MPAN Core","Site Code","Site Name",'
            '"Account","From","To","","mop-net-gbp","mop-problem","",'
            '"dc-net-gbp","dc-problem","","imp-supplier-net-gbp",'
            '"imp-supplier-vat-gbp","imp-supplier-gross-gbp",'
            '"imp-supplier-sum-msp-kwh","imp-supplier-problem"',
            r'"22 0195 4836 192","","CI004","Lower Treave","SA342376",'
            '"2011-05-01 00:00","2011-05-31 23:30","","0","","","0","","",'
            '"0.0","0.0","0.0","25.8191780822",""', ],
        'status_code': 200, },

    # Parties
    {
        'name': "Parties",
        'path': '/chellow/reports/45/output/',
        'regexes': [
            r'<a href="/chellow/reports/73/output/\?participant_id=513">'
            'SWEB</a>', ],
        'status_code': 200, },

    {
        'name': "Check rounding in bills is correct.",
        'path': '/chellow/reports/7/output/?supply_id=5',

        # Check bill net and vat are shown correctly
        'regexes': [
            r"<td>195.60</td>\s*<td>36.03</td>", ],
        'status_code': 200, },
    {
        'name': "Test the right number of rows returned for a search on '22'.",
        'path': '/chellow/reports/99/output/?search_pattern=22&max_results=12',
        'regexes': [
            r"<tbody>\s*(<tr>.*?){11}\s*</tbody>", ],
        'status_code': 200, },
    {
        'name': "Try monthly supply duration with a non-half-hourly with "
        "bills.",
        'path': '/chellow/reports/177/output/?supply_id=10&months=1&'
        'end_year=2011&end_month=01',
        'status_code': 303, },
    {
        'path': '/chellow/reports/251/output/',
        'tries': {'max': 10, 'period': 1},
        'status_code': 200,
        'regexes': [
            r"FINISHED_supplies_monthly_duration_for_10_1_to_2011_1\.csv"]},
    {
        'path': '/chellow/reports/253/output/?'
        'name=FINISHED_supplies_monthly_duration_for_10_1_to_2011_1.csv',
        'status_code': 200,
        'regexes': [
            r"supply-id,supply-name,source-code,generator-type,month,pc-code,"
            "msn,site-code,site-name,metering-type,import-mpan-core,"
            "metered-import-kwh,metered-import-net-gbp,"
            "metered-import-estimated-kwh,billed-import-kwh,"
            "billed-import-net-gbp,export-mpan-core,metered-export-kwh,"
            "metered-export-estimated-kwh,billed-export-kwh,"
            "billed-export-net-gbp,problem,timestamp",
            r'10,"2","net","","2011-01-31 23:30","03","I02D89150","CI017",'
            '"Roselands","nhh","22 1065 3921 534","0","0.0","0","150.0",'
            '"98.17","None","0","0","0","0",""', ], },
    {
        'name': "Try monthly supply duration with a half-hourly.",
        'path': '/chellow/reports/177/output/?supply_id=4&months=1&'
        'end_year=2010&end_month=05',
        'status_code': 303, },
    {
        'path': '/chellow/reports/251/output/',
        'tries': {'max': 10, 'period': 1},
        'status_code': 200,
        'regexes': [
            r"FINISHED_supplies_monthly_duration_for_4_1_to_2010_5\.csv", ], },
    {
        'path': '/chellow/reports/253/output/?'
        'name=FINISHED_supplies_monthly_duration_for_4_1_to_2010_5.csv',
        'status_code': 200,
        'regexes': [
            r"supply-id,supply-name,source-code,generator-type,month,pc-code,"
            "msn,site-code,site-name,metering-type,import-mpan-core,"
            "metered-import-kwh,metered-import-net-gbp,"
            "metered-import-estimated-kwh,billed-import-kwh,"
            "billed-import-net-gbp,export-mpan-core,metered-export-kwh,"
            "metered-export-estimated-kwh,billed-export-kwh,"
            "billed-export-net-gbp,problem,timestamp",
            r'4,"1","net","","2010-05-31 23:30","00","","CI005",'
            '"Wheal Rodney","hh","22 6158 2968 220","0","179.2268","0","0",'
            '"0","22 3479 7618 470","0","0","0","0",""', ], },
    {
        'name': "Check supplies monthly duration page.",
        'path': '/chellow/reports/155/output/',
        'regexes': [
            r"end_month", ],
        'status_code': 200, },
    {
        'name': "Check CSV Sites Duration",
        'path': '/chellow/reports/57/output/',

        # Should have link to CSS
        'regexes': [
            r"/reports/19/output/", ],
        'status_code': 200, },
    {
        'path': '/chellow/reports/59/output/?start_year=2013&start_month=04&'
        'start_day=01&start_hour=00&start_minute=00&finish_year=2013&'
        'finish_month=04&finish_day=1&finish_hour=23&finish_minute=30',
        'regexes': [
            r'"CH017","Parbola","","sub","","2013-04-01 00:00",'
            '"2013-04-01 23:30","0","0","0","0","0","0","hh"', ],
        'status_code': 200, },
    {
        'name': "Check CSV Sites HH Data Selector.",
        'path': '/chellow/reports/145/output/',

        # Should have link to CSS
        'regexes': [
            r"/reports/19/output/", ],
        'status_code': 200, },
    {
        'name': "Check CSV Supplies HH Data. With supply_id",
        'path': '/chellow/reports/169/output/',
        'method': 'post',
        'data': {
            'supply_id': '1', 'imp_related': 'true', 'channel_type': 'ACTIVE',
            'start_year': '2008', 'start_month': '7', 'start_day': '1',
            'start_hour': '0', 'start_minute': '0', 'finish_year': '2008',
            'finish_month': '07', 'finish_day': '31', 'finish_hour': '23',
            'finish_minute': '30'},
        'status_code': 303, },
    {
        'path': '/chellow/reports/251/output/',
        'tries': {'max': 20, 'period': 1},
        'status_code': 200,
        'regexes': [
            r"FINISHED_supplies_hh_data_200807313023\.csv", ], },
    {
        'path': '/chellow/reports/253/output/?'
        'name=FINISHED_supplies_hh_data_200807313023.csv',
        'status_code': 200,

        # Check the HH data is there
        'regexes': [
            r"NA,2008-07-06,0\.262", ]},

    # Add a new era with this contract },
    {
        'name': "Test duos-fixed",
        'path': '/chellow/reports/305/output/',
        'method': 'post',
        'data': {
            'supply_id': "5",
            'start_year': "2013",
            'start_month': "01",
            'start_day': "01",
            'start_hour': "00",
            'start_minute': "00",
            'insert_era': "Insert", },
        'regexes': [
            r"/reports/7/output/\?supply_id=5", ],
        'status_code': 303, },

    # Supply 5
    {
        'path': '/chellow/reports/307/output/',
        'method': 'post',
        'data': {
            'era_id': "23",
            'start_year': "2013",
            'start_month': "01",
            'start_day': "01",
            'start_hour': "00",
            'start_minute': "00",
            'is_ended': "false",
            'gsp_group_id': "11",
            'mop_contract_id': "57",
            'mop_account': "22 0883 6932 301",
            'hhdc_contract_id': "53",
            'hhdc_account': "22 0883 6932 301",
            'msn': "",
            'pc_id': "9",
            'mtc_code': "845",
            'cop_id': "5",
            'ssc_code': "",
            'imp_llfc_code': "570",
            'imp_mpan_core': "22 0883 6932 301",
            'imp_sc': "350",
            'imp_supplier_contract_id': "58",
            'imp_supplier_account': "4341", },
        'status_code': 303, },
    {
        'path': '/chellow/reports/291/output/?supply_id=5&start_year=2013&'
        'start_month=04&start_day=01&start_hour=00&start_minute=00&'
        'finish_year=2013&finish_month=04&finish_day=30&finish_hour=23&'
        'finish_minute=30',
        'status_code': 200,
        'regexes': [
            r'"Imp MPAN Core","Exp MPAN Core","Site Code","Site Name",'
            '"Account","From","To","","mop-net-gbp","mop-problem","",'
            '"dc-net-gbp","dc-problem","","imp-supplier-net-gbp",'
            '"imp-supplier-tlm","imp-supplier-ccl-kwh",'
            '"imp-supplier-ccl-rate","imp-supplier-ccl-gbp",'
            '"imp-supplier-data-collection-gbp",'
            '"imp-supplier-duos-availability-kva",'
            '"imp-supplier-duos-availability-days",'
            '"imp-supplier-duos-availability-rate",'
            '"imp-supplier-duos-availability-gbp",'
            '"imp-supplier-duos-excess-availability-kva",'
            '"imp-supplier-duos-excess-availability-days",'
            '"imp-supplier-duos-excess-availability-rate",'
            '"imp-supplier-duos-excess-availability-gbp",'
            '"imp-supplier-duos-green-kwh","imp-supplier-duos-green-rate",'
            '"imp-supplier-duos-green-gbp","imp-supplier-duos-green-kwh",'
            '"imp-supplier-duos-green-rate","imp-supplier-duos-amber-gbp",'
            '"imp-supplier-duos-amber-kwh","imp-supplier-duos-red-rate",'
            '"imp-supplier-duos-red-gbp","imp-supplier-duos-reactive-kvarh",'
            '"imp-supplier-duos-reactive-rate",'
            '"imp-supplier-duos-reactive-gbp","imp-supplier-duos-fixed-days",'
            '"imp-supplier-duos-fixed-rate","imp-supplier-duos-fixed-gbp",'
            '"imp-supplier-settlement-gbp","imp-supplier-aahedc-msp-kwh",'
            '"imp-supplier-aahedc-gsp-kwh","imp-supplier-aahedc-rate",'
            '"imp-supplier-aahedc-gbp","imp-supplier-rcrc-kwh",'
            '"imp-supplier-rcrc-rate","imp-supplier-rcrc-gbp",'
            '"imp-supplier-night-msp-kwh","imp-supplier-night-gsp-kwh",'
            '"imp-supplier-night-gbp","imp-supplier-other-msp-kwh",'
            '"imp-supplier-other-gsp-kwh","imp-supplier-other-gbp",'
            '"imp-supplier-summer-pk-msp-kwh",'
            '"imp-supplier-summer-pk-gsp-kwh","imp-supplier-summer-pk-gbp",'
            '"imp-supplier-winter-low-pk-msp-kwh",'
            '"imp-supplier-winter-low-pk-gsp-kwh",'
            '"imp-supplier-winter-low-pk-gbp",'
            '"imp-supplier-winter-off-pk-msp-kwh",'
            '"imp-supplier-winter-off-pk-gsp-kwh",'
            '"imp-supplier-winter-off-pk-gbp",'
            '"imp-supplier-winter-pk-msp-kwh",'
            '"imp-supplier-winter-pk-gsp-kwh",'
            '"imp-supplier-winter-pk-gbp",'
            '"imp-supplier-bsuos-kwh","imp-supplier-bsuos-rate",'
            '"imp-supplier-bsuos-gbp","imp-supplier-triad-actual-1-date",'
            '"imp-supplier-triad-actual-1-msp-kw",'
            '"imp-supplier-triad-actual-1-status",'
            '"imp-supplier-triad-actual-1-laf",'
            '"imp-supplier-triad-actual-1-gsp-kw",'
            '"imp-supplier-triad-actual-2-date",'
            '"imp-supplier-triad-actual-2-msp-kw",'
            '"imp-supplier-triad-actual-2-status",'
            '"imp-supplier-triad-actual-2-laf",'
            '"imp-supplier-triad-actual-2-gsp-kw",'
            '"imp-supplier-triad-actual-3-date",'
            '"imp-supplier-triad-actual-3-msp-kw",'
            '"imp-supplier-triad-actual-3-status",'
            '"imp-supplier-triad-actual-3-laf",'
            '"imp-supplier-triad-actual-3-gsp-kw",'
            '"imp-supplier-triad-actual-gsp-kw",'
            '"imp-supplier-triad-actual-rate",'
            '"imp-supplier-triad-actual-gbp",'
            '"imp-supplier-triad-estimate-1-date",'
            '"imp-supplier-triad-estimate-1-msp-kw",'
            '"imp-supplier-triad-estimate-1-status",'
            '"imp-supplier-triad-estimate-1-laf",'
            '"imp-supplier-triad-estimate-1-gsp-kw",'
            '"imp-supplier-triad-estimate-2-date",'
            '"imp-supplier-triad-estimate-2-msp-kw",'
            '"imp-supplier-triad-estimate-2-status",'
            '"imp-supplier-triad-estimate-2-laf",'
            '"imp-supplier-triad-estimate-2-gsp-kw",'
            '"imp-supplier-triad-estimate-3-date",'
            '"imp-supplier-triad-estimate-3-msp-kw",'
            '"imp-supplier-triad-estimate-3-status",'
            '"imp-supplier-triad-estimate-3-laf",'
            '"imp-supplier-triad-estimate-3-gsp-kw",'
            '"imp-supplier-triad-estimate-gsp-kw",'
            '"imp-supplier-triad-estimate-rate",'
            '"imp-supplier-triad-estimate-months",'
            '"imp-supplier-triad-estimate-gbp",'
            '"imp-supplier-triad-all-estimates-months",'
            '"imp-supplier-triad-all-estimates-gbp",'
            '"imp-supplier-problem"',
            r'"22 0883 6932 301","","CI005","Wheal Rodney","4341",'
            '"2013-04-01 00:00","2013-04-30 23:30","","0","","","0","","",'
            '"369.605","","","0.00525288","","5.89","350","30",'
            '"0.026","273.0","0","31","0.026","0.0","0","0.00161","0.0","","",'
            '"0.0","0","0.2441","0.0","0.0","0.00382","0.0","30","0.0905",'
            '"2.715","88","0",'
            '"0.0","0.00019737201","0.0","0.0","","0.0","0",'
            '"0.0","0.0","0","0.0","0.0","0","0.0","0.0","","","","","","","",'
            '"","","0.0",'
            '"","0.0","","","","","","","","","","","","","","","",'
            '"","","","2012-11-29 17:00","0","X","1.087","0.0",'
            '"2012-12-12 17:00","0","X","1.087","0.0","2013-01-16 17:00","0",'
            '"X","1.087","0.0","0.0","33.551731","1","0.0","","",""', ], },
    {
        'path': '/chellow/reports/159/output/',
        'regexes': [
            r"finish_year", ],
        'status_code': 200, },
    {
        'name': "Try site search",
        'path': '/chellow/reports/3/output/?pattern=',
        'regexes': [
            r'<a href="/chellow/reports/5/output/\?site_id=8">'
            'B00LG Bieling</a>', ],
        'status_code': 200, },
    {
        'name': "Try TRIAD report when supply starts after first triad",
        'path': '/chellow/reports/41/output/?supply_id=6&year=2007',
        'status_code': 200,
        'regexes': [
            r'CI017,"Roselands","1",net,"","22 6354 2983 570",'
            '"2007-01-23 17:00","0","X","1.074","0.0","2006-12-20 17:00","0",'
            '"before start of supply","before start of supply","0",'
            '"2007-02-08 17:30","0","X","1.074","0.0","0.0","5.94264","0.0",'
            '"","","","","","","","","","","","","","","","","","",""$', ], },

    # Insert a 14 supply },
    {
        'name': "Try a pre 2010-04-01 DNO 14 bill.",
        'path': '/chellow/reports/311/output/',
        'method': 'post',
        'data': {
            'site_id': "5",
            'source_id': "1",
            'name': "Bernard",
            'start_year': "2003",
            'start_month': "08",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00",
            'msn': "88jiuf ff",
            'gsp_group_id': "5",
            'pc_id': "9",
            'mtc_code': "845",
            'cop_id': "5",
            'ssc_code': "",
            'mop_contract_id': "57",
            'mop_account': "mc-14 7206 6139 971",
            'hhdc_contract_id': "53",
            'hhdc_account': "dc-14 7206 6139 971",
            'imp_llfc_code': "365",
            'imp_mpan_core': "14 7206 6139 971",
            'imp_sc': "2300",
            'imp_supplier_contract_id': "55",
            'imp_supplier_account': "sup-14 7206 6139 971",
            'insert': "insert", },
        'regexes': [
            r"/chellow/reports/7/output/\?supply_id=17", ],
        'status_code': 303, },

    # Try a pre 2010-04-01 DNO 14 bill.
    {
        'path': '/chellow/reports/291/output/?supply_id=17&start_year=2009&'
        'start_month=06&start_day=01&start_hour=00&start_minute=00&'
        'finish_year=2009&finish_month=06&finish_day=30&finish_hour=23&'
        'finish_minute=30',
        'status_code': 200,
        'regexes': [
            r'"Imp MPAN Core","Exp MPAN Core","Site Code","Site Name",'
            '"Account","From","To","","mop-net-gbp","mop-problem","",'
            '"dc-net-gbp","dc-problem","","imp-supplier-net-gbp",'
            '"imp-supplier-tlm","imp-supplier-ccl-kwh",'
            '"imp-supplier-ccl-rate","imp-supplier-ccl-gbp",'
            '"imp-supplier-data-collection-gbp",'
            '"imp-supplier-duos-availability-kva",'
            '"imp-supplier-duos-availability-days",'
            '"imp-supplier-duos-availability-rate",'
            '"imp-supplier-duos-availability-gbp",'
            '"imp-supplier-duos-excess-availability-kva",'
            '"imp-supplier-duos-excess-availability-days",'
            '"imp-supplier-duos-excess-availability-rate",'
            '"imp-supplier-duos-excess-availability-gbp",'
            '"imp-supplier-duos-day-kwh","imp-supplier-duos-day-gbp",'
            '"imp-supplier-duos-night-kwh","imp-supplier-duos-night-gbp",'
            '"imp-supplier-duos-reactive-rate",'
            '"imp-supplier-duos-reactive-gbp",'
            '"imp-supplier-duos-standing-gbp",'
            '"imp-supplier-settlement-gbp","imp-supplier-night-msp-kwh",'
            '"imp-supplier-night-gsp-kwh","imp-supplier-night-gbp",'
            '"imp-supplier-other-msp-kwh","imp-supplier-other-gsp-kwh",'
            '"imp-supplier-other-gbp","imp-supplier-summer-pk-msp-kwh",'
            '"imp-supplier-summer-pk-gsp-kwh","imp-supplier-summer-pk-gbp",'
            '"imp-supplier-winter-low-pk-msp-kwh",'
            '"imp-supplier-winter-low-pk-gsp-kwh",'
            '"imp-supplier-winter-low-pk-gbp",'
            '"imp-supplier-winter-off-pk-msp-kwh",'
            '"imp-supplier-winter-off-pk-gsp-kwh",'
            '"imp-supplier-winter-off-pk-gbp",'
            '"imp-supplier-winter-pk-msp-kwh",'
            '"imp-supplier-winter-pk-gsp-kwh",'
            '"imp-supplier-winter-pk-gbp",'
            '"imp-supplier-bsuos-kwh","imp-supplier-bsuos-rate",'
            '"imp-supplier-bsuos-gbp","imp-supplier-triad-actual-1-date",'
            '"imp-supplier-triad-actual-1-msp-kw",'
            '"imp-supplier-triad-actual-1-status",'
            '"imp-supplier-triad-actual-1-laf",'
            '"imp-supplier-triad-actual-1-gsp-kw",'
            '"imp-supplier-triad-actual-2-date",'
            '"imp-supplier-triad-actual-2-msp-kw",'
            '"imp-supplier-triad-actual-2-status",'
            '"imp-supplier-triad-actual-2-laf",'
            '"imp-supplier-triad-actual-2-gsp-kw",'
            '"imp-supplier-triad-actual-3-date",'
            '"imp-supplier-triad-actual-3-msp-kw",'
            '"imp-supplier-triad-actual-3-status",'
            '"imp-supplier-triad-actual-3-laf",'
            '"imp-supplier-triad-actual-3-gsp-kw",'
            '"imp-supplier-triad-actual-gsp-kw",'
            '"imp-supplier-triad-actual-rate","imp-supplier-triad-actual-gbp",'
            '"imp-supplier-triad-estimate-1-date",'
            '"imp-supplier-triad-estimate-1-msp-kw",'
            '"imp-supplier-triad-estimate-1-status",'
            '"imp-supplier-triad-estimate-1-laf",'
            '"imp-supplier-triad-estimate-1-gsp-kw",'
            '"imp-supplier-triad-estimate-2-date",'
            '"imp-supplier-triad-estimate-2-msp-kw",'
            '"imp-supplier-triad-estimate-2-status",'
            '"imp-supplier-triad-estimate-2-laf",'
            '"imp-supplier-triad-estimate-2-gsp-kw",'
            '"imp-supplier-triad-estimate-3-date",'
            '"imp-supplier-triad-estimate-3-msp-kw",'
            '"imp-supplier-triad-estimate-3-status",'
            '"imp-supplier-triad-estimate-3-laf",'
            '"imp-supplier-triad-estimate-3-gsp-kw",'
            '"imp-supplier-triad-estimate-gsp-kw",'
            '"imp-supplier-triad-estimate-rate",'
            '"imp-supplier-triad-estimate-months",'
            '"imp-supplier-triad-estimate-gbp",'
            '"imp-supplier-triad-all-estimates-months",'
            '"imp-supplier-triad-all-estimates-gbp","imp-supplier-problem"',
            r'"14 7206 6139 971","","CH023","Treglisson",'
            '"sup-14 7206 6139 971","2009-06-01 00:00","2009-06-30 23:30","",'
            '"0","","","0","","","334.3","","","0.0047","","5.89","",'
            '"","0.0457","105.11","","","","","0","0.0","0","0.0","0.0012",'
            '"0.0",'
            '"135.3","88","0","0.0","0.0","0","0.0","0.0","0","0.0","0.0","0",'
            '"0",'
            '"0.0","0","0","0.0","0","0","0.0","0.0","","0.0","","",'
            '"","","","","","","","","","","","","","","","",'
            '"2009-01-06 17:00","0","X","1.037","0.0","2008-12-01 17:00","0",'
            '"X","1.037","0.0","2008-12-15 17:00","0","X","1.037","0.0","0.0",'
            '"20.526611","1","0.0","","","","duos-availability-agreed-kva",'
            '"2300","duos-availability-billed-kva","2300"', ], },
    {
        'name': "Report of HHDC snags",
        'path': '/chellow/reports/233/output/?hhdc_contract_id=53&'
        'days_hidden=1',
        'status_code': 200,
        'regexes': [
            r'"83","22 0883 6932 301","None","CI005","Wheal Rodney","Missing",'
            '"True","ACTIVE","2002-01-01 00:00","2003-08-02 23:30",', ], },
    {
        'name': "Site use graph",
        'path': '/chellow/reports/9/output/?site_id=5&months=1&'
        'finish_year=2013&finish_month=6',
        'status_code': 200,
        'regexes': [
            r'<option value="06" selected>06</option>', ], },
    {
        'name': "Site generation graph",
        'path': '/chellow/reports/11/output/?site_id=7&months=1&'
        'finish_year=2013&finish_month=7',
        'regexes': [
            r'<input type="hidden" name="site_id" value="7">', ],
        'status_code': 200, },

    # Can we make a supply have source sub and view site level hh data okay? },
    {
        'name': "CSV Sites HH Data",
        'path': '/chellow/reports/305/output/',
        'method': 'post',

        # Can we update a supply name?

        # Can we update a supply source?
        'data': {
            'supply_id': "1",
            'name': "Hello",
            'source_id': "2",
            'generator_type_id': "1",
            'gsp_group_id': "11", },
        'regexes': [
            r"/reports/7/output/\?supply_id=1", ],
        'status_code': 303, },
    {
        'path': '/chellow/reports/29/output/?site_id=7&type=used&months=1&'
        'finish_year=2008&finish_month=07',
        'status_code': 200,
        'regexes': [
            r"CH017,used,2008-07-01,", ], },
    {
        'path': '/chellow/reports/29/output/?site_id=7&type=displaced&'
        'months=1&finish_year=2008&finish_month=07',
        'status_code': 200,
        'regexes': [
            r"CH017,displaced,2008-07-01,", ], },
    {
        'name': "Look at list of supplier contracts.",
        'path': '/chellow/reports/75/output/',

        # Are the contracts in alphabetical order?
        'regexes': [
            r'<tbody>\s*<tr>\s*<td>\s*'
            '<a href="/chellow/reports/77/output/\?supplier_contract_id=55">'
            'Half-hourlies 2007</a>', ],
        'status_code': 200, },
    {
        'name': "Daily supplier virtual bills page.",
        'path': '/chellow/reports/241/output/?supply_id=6&is_import=true&'
        'start_year=2013&start_month=10&start_day=1&finish_year=2013&'
        'finish_month=10&finish_day=31',
        'status_code': 200,
        'regexes': [
            r"MPAN Core,Site Code,Site Name",
            r'"22 6354 2983 570",', ], },

    # See if selector is working },
    {
        'name': "Test register read report.",
        'path': '/chellow/reports/217/output/',
        'status_code': 200,
        'regexes': [
            r"end_year", ], },
    {
        'name': "Test register read report for a supply.",
        'path': '/chellow/reports/219/output/?supply_id=10&months=1&'
        'end_year=2011&end_month=1',
        'status_code': 200,
        'regexes': [
            r'\.csv".\)',
            r"Duration Start,Duration Finish,Supply Id,Import MPAN Core,"
            "Export MPAN Core,Batch Reference,Bill Id,Bill Reference,"
            "Bill Issue Date,Bill Type,Register Read Id,TPR,Coefficient,"
            "Previous Read Date,Previous Read Value,Previous Read Type,"
            "Present Read Date,Present Read Value,Present Read Type",
            r'"2011-01-01 00:00","2011-01-31 23:30","10","22 1065 3921 534",'
            '"","07-002","13","3423760005","2011-02-02 00:00","N","8","00001",'
            '"1","2011-01-04 23:30","24286","E","2011-01-06 23:30","25927",'
            '"E"', ], },

    # Try for a period where there's a read with no TPR (an MD read)
    {
        'path': '/chellow/reports/219/output/?supply_id=10&months=1&'
        'end_year=2007&end_month=1',
        'status_code': 200,
        'regexes': [
            r'"2007-01-01 00:00","2007-01-31 23:30","10","22 1065 3921 534",'
            '"","06-002","14","SA342376","2007-01-01 00:00","N","12","md","1",'
            '"2007-01-04 00:00","45","E","2007-01-17 00:00","76","E"', ], },
    {
        'name': "View a MOP rate script. Contract 57.",
        'path': '/chellow/reports/205/output/?mop_rate_script_id=309',
        'status_code': 200, },
    {
        'name': "View supplies duration selector.",
        'path': '/chellow/reports/147/output/',
        'status_code': 200,
        'regexes': [
            r"start_year", ], },
    {
        'name': "Look at a TPR.",
        'path': '/chellow/reports/97/output/?tpr_id=1',
        'status_code': 200,
        'regexes': [
            r"<tbody>\s*<tr>\s*<td>1</td>\s*<td>1</td>", ], },
    {
        'name': "CSV Bills.",
        'path': '/chellow/reports/153/output/',
        'status_code': 200,
        'regexes': [
            r"end_year", ], },
    {
        'name': "CSV Supplies Duration with register reads",
        'path': '/chellow/reports/149/output/?start_year=2010&start_month=01&'
        'start_day=1&start_hour=0&start_minute=0&finish_year=2010&'
        'finish_month=01&finish_day=31&finish_hour=23&finish_minute=30',
        'regexes': [
            r'"10","2",', ], },
    {
        'name': "Try the site level monthly data HTML report.",
        'path': '/chellow/reports/13/output/?site_id=3&finish_year=2005&'
        'finish_month=11',
        'regexes': [
            r"For 12 months finishing at the end of",
            r"<th>2005-09-15 00:00</th>", ],
        'status_code': 200, },
    {
        'name': "Change the name of a site.",
        'path': '/chellow/reports/311/output/',
        'method': 'post',
        'data': {
            'site_id': "8",
            'name': "Ishmael",
            'code': "MOBY",
            'update': "Update", },
        'status_code': 303, },

    # Insert era },
    {
        'name': "Try inserting an era where the existing era is attached to "
        "more than one site.",
        'path': '/chellow/reports/305/output/',
        'method': 'post',
        'data': {
            'supply_id': "2",
            'start_year': "2005",
            'start_month': "05",
            'start_day': "04",
            'start_hour': "00",
            'start_minute': "00",
            'insert_era': "insert_era", },
        'status_code': 303, },
    {
        'name': "Check user roles page.",
        'path': '/chellow/reports/261/output/',
        'status_code': 200,
        'regexes': [
            r"party-viewer", ], },
    {
        'name': "Scenario runner",
        'path': '/chellow/reports/245/output/',
        'status_code': 200, },
    {
        'name': "Bill type",
        'path': '/chellow/reports/201/output/?bill_type_id=1',
        'status_code': 200, },

    # Supplier contract 60. },
    {
        'name': "Test sse edi bill with MD line",
        'path': '/chellow/reports/321/output/',
        'method': 'post',
        'data': {
            'supplier_batch_id': "3", },
        'files': {'import_file': 'bills2.sse.edi'},
        'status_code': 303,
        'regexes': [
            r"/reports/323/output/\?importer_id=0", ], },

    # Supplier contract 60.
    {
        'path': '/chellow/reports/323/output/?importer_id=0',
        'tries': {'max': 10, 'period': 1},
        'status_code': 200,
        'regexes': [
            r"All the bills have been successfully loaded and attached to "
            "the batch\.", ], },
    {
        'name': "Look at an HHDC batch",
        'path': '/chellow/reports/203/output/?hhdc_batch_id=8',
        'status_code': 200,
        'regexes': [
            r"<tbody>\s*<tr>", ], },

    # Supplier contract 60, batch 7, bill 10 },
    {
        'name': "Edit register read with a TPR that's not 00001",
        'path': '/chellow/reports/31/output/?supplier_read_id=1',
        'regexes': [
            r'<option value="37" selected>00040</option>', ], },

    # Insert a new batch },
    {
        'name': "Add and delete an HHDC contract",
        'path': '/chellow/reports/281/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "53",
            'reference': "to_delete",
            'description': "", },
        'status_code': 303,
        'regexes': [
            r"/reports/203/output/\?hhdc_batch_id=10", ], },

    # Delete it. HHDC contract 52
    {
        'path': '/chellow/reports/283/output/',
        'method': 'post',
        'data': {
            'hhdc_batch_id': "10",
            'delete': "Delete", },
        'status_code': 303, },

    # CRC Special Events
    {
        'name': "CRC Special Events",
        'path': '/chellow/reports/215/output/?year=2012',
        'status_code': 200,
        'regexes': [
            r'"22 0883 6932 301","CI005",', ], },

    {
        'name': "A supply level virtual bill that crosses an era boundary",
        'path': '/chellow/reports/291/output/?supply_id=10&start_year=2010&'
        'start_month=01&start_day=01&start_hour=00&start_minute=0&'
        'finish_year=2010&finish_month=01&finish_day=31&finish_hour=23&'
        'finish_minute=30',
        'status_code': 200,
        'regexes': [
            r'"Imp MPAN Core","Exp MPAN Core","Site Code","Site Name",'
            '"Account","From","To","","mop-net-gbp","mop-problem","",'
            '"dc-net-gbp","dc-problem","","imp-supplier-net-gbp",'
            '"imp-supplier-vat-gbp","imp-supplier-gross-gbp",'
            '"imp-supplier-sum-msp-kwh","imp-supplier-problem"',
            r'"22 1065 3921 534","","CI017","Roselands","SA342376",'
            '"2010-01-01 00:00","2010-01-03 23:30","","0","","","0","","",'
            '"0.0","0.0","0.0","0",""', ], },
    {
        'name': "A bill check with multiple covered bills",
        'path': '/chellow/reports/111/output/?bill_id=8',
        'status_code': 200,
        'regexes': [
            r'"06-004","00101","N","244","3810.08","355.03",'
            '"2011-05-01 00:00","2011-06-30 00:00","22 6354 2983 570","CI017",'
            '"Roselands","2011-05-01 00:00","2011-06-30 00:00","9;8",'
            '"4701.16","3010.226","1690.934","","","","","11.4",'
            '"0.00485","","","","","5.89","","","2300","","60","","0.0211",'
            '"","2911.8","","","0","","31","","0.0211","","0.0","","","","",'
            '"","","","","","","","","0.00353","","0.0","","","","","","88",'
            '"","","0","","0.0","","0.0","","","0","","0.0","","0.0","","",'
            '"0",'
            '"","0.0","","0.0","","","0","","0","","0.0","","","0","","0","",'
            '"0.0","","","0","","0","","0.0","","","0.0","","","",'
            '"0.0","","","","","","","","","","","","","","","","","","","",'
            '"","","","","","","","","","","","","","","","","","","","",'
            '"2010-12-07 17:00","","0","","X","","1.087","","0.0","",'
            '"2010-12-20 17:00","","0","","X","","1.087","","0.0","",'
            '"2011-01-06 17:00","","0","","X","","1.087","","0.0","","0.0","",'
            '"28.408897","","1","","0.0","","","","","","","","",'
            '"virtual-duos-amber-gbp","0.0","","","virtual-duos-amber-kwh",'
            '"0","","","virtual-duos-amber-rate","0.00205","","",',
            '"virtual-duos-fixed-days","60","","","virtual-duos-fixed-gbp",'
            '"4.536","","","virtual-duos-fixed-rate","0.0756","","",'
            '"virtual-duos-green-gbp","0.0","","","virtual-duos-green-kwh",'
            '"0","","","virtual-duos-green-rate","0.00138","",""', ], },
    {
        'name': "Contract virtual bills",
        'path': '/chellow/reports/87/output/?supplier_contract_id=55&'
        'start_year=2013&start_month=12&start_day=01&start_hour=00&'
        'start_minute=00&finish_year=2013&finish_month=12&finish_day=01&'
        'finish_hour=23&finish_minute=30',
        'status_code': 200,
        'regexes': [
            r'"22 0470 7514 535","CH017","Parbola","010","2013-12-01 00:00",'
            '"2013-12-01 23:30","93.89","","","","","5.89","150","1",'
            '"0","0","","","","","","","","","0.00147","0.0","","88","0",'
            '"0.0",'
            '"0.0","0","0.0","0.0","0","0","0.0","0","0","0.0","0","0","0.0",'
            '"0","0","0.0","0.0","","0.0","","","","","","","","",'
            '"","","","","","","","","","","","","","","","","","","","","",'
            '"","","","","","","","","","","","duos-amber-gbp","0.0",'
            '"duos-amber-kwh","0","duos-amber-rate","-0.00649",'
            '"duos-fixed-days","1",'
            '"duos-fixed-gbp","0","duos-fixed-rate","0","duos-green-gbp",'
            '"0.0","duos-green-kwh","0","duos-green-rate","-0.00649"', ], },
    {
        'name': "Contract displaced virtual bills",
        'path': '/chellow/reports/109/output/?supplier_contract_id=55&'
        'months=1&finish_year=2013&finish_month=01',
        'status_code': 200,
        'regexes': [
            r'"CI004",', ], },

    # Move finish date of era },
    {
        'name': "Check that covering hh data by a different era doesn't "
        "result in missing data being reported.",
        'path': '/chellow/reports/307/output/',
        'method': 'post',
        'data': {
            'era_id': "1",
            'start_year': "2003",
            'start_month': "08",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00",
            'is_ended': "true",
            'finish_year': "2004",
            'finish_month': "07",
            'finish_day': "06",
            'finish_hour': "23",
            'finish_minute': "30",
            'mop_contract_id': "57",
            'mop_account': "mc-22 9205 6799 106",
            'hhdc_contract_id': "53",
            'hhdc_account': "01",
            'msn': "",
            'pc_id': "9",
            'mtc_code': "845",
            'cop_id': "5",
            'ssc_code': "",
            'imp_llfc_code': "540",
            'imp_mpan_core': "22 9205 6799 106",
            'imp_sc': "450",
            'imp_supplier_contract_id': "55",
            'imp_supplier_account': "11640077",
            'exp_llfc_code': "581",
            'exp_mpan_core': "22 0470 7514 535",
            'exp_sc': "150",
            'exp_supplier_contract_id': "55",
            'exp_supplier_account': "", },
        'status_code': 303, },
    {
        'path': '/chellow/reports/37/output/?hhdc-contract-id=53&'
        'hidden_days=5',
        'status_code': 200,
        'regexes': [
            r'<tr>\s*<td>\s*<ul>\s*<li>\s*'
            '<a href="/chellow/reports/117/output/\?snag_id=100">'
            'view</a>  \[<a href="/chellow/reports/365/output/\?snag_id=100">'
            'edit</a>\]\s*</li>\s*</ul>\s*</td>\s*<td>\s*</td>\s*<td>\s*'
            '22 0470 7514 535\s*</td>\s*<td>\s*<ul>\s*'
            '<li>CH017 Parbola</li>\s*</ul>\s*</td>\s*<td>Missing</td>\s*'
            '<td>\s*<ul>\s*<li>\s*Export\s*ACTIVE\s*</li>\s*</ul>\s*</td>\s*'
            '<td>\s*2004-07-07 00:00 to\s*2005-09-14 23:30\s*</td>\s*</tr>']},

    # Insert era },
    {
        'name': "Inserting an era that covers an ongoing era that has data "
        "from start.",
        'path': '/chellow/reports/305/output/',
        'method': 'post',
        'data': {
            'supply_id': "7",
            'start_year': "2008",
            'start_month': "11",
            'start_day': "02",
            'start_hour': "00",
            'start_minute': "00",
            'insert_era': "insert_era", },
        'status_code': 303, },
    {
        'path': '/chellow/reports/233/output/?hhdc_contract_id=53&'
        'days_hidden=0',
        'regexes': [
            r'"0","107","22 4862 4512 332","None","CH023","Treglisson",'
            '"Missing","True","ACTIVE","2010-02-04 20:30",""',
            r'"0","3","22 9205 6799 106","22 0470 7514 535","CH017","Parbola",'
            '"Missing","False","ACTIVE","2003-08-03 00:00","2004-07-06 23:30",'
            '"[^"]*","[^"]*","True"\s*"0","100","None","22 0470 7514 535",'
            '"CH017","Parbola","Missing","False","ACTIVE","2004-07-07 00:00",'
            '"2005-09-14 23:30","[^"]*","[^"]*","False"\s*"0","102","None",'
            '"22 0470 7514 535","CH017","Parbola","Missing","False","ACTIVE",'
            '"2005-09-15 00:30","2005-12-15 06:30","[^"]*","[^"]*","False"\s*'
            '"0","101","None","22 0470 7514 535","CH017","Parbola","Missing",'
            '"False","ACTIVE","2005-12-15 10:00","2008-07-06 23:30","[^"]*",'
            '"[^"]*","False"\s*"0","56","None","22 0470 7514 535","CH017",'
            '"Parbola","Missing","False","ACTIVE","2008-07-07 00:00",'
            '"2008-08-06 23:30","[^"]*","[^"]*","True"\s*'
            '"0","79","None","22 0470 7514 535","CH017","Parbola","Missing",'
            '"False","ACTIVE","2008-08-07 00:00","2008-09-05 23:30",'
            '"[^"]*","[^"]*","False"\s*"0","68","None","22 0470 7514 535",'
            '"CH017","Parbola","Missing","False","ACTIVE","2008-09-06 00:00",'
            '"","[^"]*","[^"]*","False"\s*', ],
        'status_code': 200, },
    {
        'name': "Check that an era with imp_sc of 0 is displayed properly in "
        "edit mode. Supply 17",
        'path': '/chellow/reports/307/output/?era_id=22',
        'regexes': [
            r'<input name="imp_sc" value="0" size="9" maxlength="9">', ],
        'status_code': 200, },
    {
        'name': "Try out the supplies snapshot report including a last normal "
        "read type.",
        'path': '/chellow/reports/33/output/?supply_id=9&year=2007&month=09&'
        'day=01&hour=00&minute=00',
        'status_code': 200,
        'regexes': [
            r'"2007-09-30 23:30","CI004","Lower Treave","","","9","net","",'
            '"22","HV","nhh","no","05","535","5","0127","3","MOP Contract",'
            '"mc-22 0195 4836 192","Dynamat data","dc-22 0195 4836 192",'
            '"P96C93722","2005-08-06 00:00","2007-08-01 00:00","N","","",'
            '"false","false","false","false","false","false",'
            '"22 0195 4836 192","30","510","PC 5-8 & HH HV",'
            '"Non half-hourlies 2007","341664","","2007-08-01 00:00","","","",'
            '"","","","",""', ], },

    # Try a supplies snapshot where previous era isn't AMR
    {
        'path': '/chellow/reports/33/output/?supply_id=9&year=2011&month=05&'
        'day=01&hour=00&minute=00',
        'status_code': 200,
        'regexes': [
            r'"2011-05-31 23:30","CI004","Lower Treave","","","9","net","",'
            '"22","LV","unmetered","no","08","857","6c","0428","2",'
            '"MOP Contract","mc-22 0195 4836 192","Dynamat data",'
            '"dc-22 0195 4836 192","P96C93722","2005-08-06 00:00","unmetered",'
            '"","","","false","false","false","false","false","false",'
            '"22 0195 4836 192","304","980","NHH UMS Cat B : Dusk to Dawn",'
            '"Non half-hourlies 2007","SA342376","","2007-08-01 00:00","","",'
            r'"","","","","",""$', ], },

    # Try a supplies snapshot to check that latest import supplier bill is
    # correct
    {
        'path': '/chellow/reports/33/output/?supply_id=6&year=2012&month=05&'
        'day=01&hour=00&minute=00',
        'status_code': 200,
        'regexes': [
            r"Other Site Ids,Other Site Names",
            r'"2012-05-31 23:30","CI017","Roselands","","","6","net","","22",'
            '"LV","hh","no","00","845","5","","","MOP Contract",'
            '"mc-22 6354 2983 570","HH contract","01","","2007-01-01 00:00",'
            '"hh","","","","true","true","false","false","false","true",'
            '"22 6354 2983 570","2300","570","PC 5-8 & HH LV",'
            '"Half-hourlies 2007","141 5532","","2011-06-30 00:00","","","",'
            '"","","","",""$', ], },
    {
        'name': "Run supply virtual bill over 2 months",
        'path': '/chellow/reports/291/output/?supply_id=7&start_year=2013&'
        'start_month=09&start_day=29&start_hour=00&start_minute=00&'
        'finish_year=2013&finish_month=11&finish_day=28&finish_hour=23&'
        'finish_minute=30',
        'regexes': [
            r'"22 4862 4512 332","","CH023","Treglisson","141 5532",'
            '"2013-10-01 00:00","2013-10-31 23:30","","0","","","0","","",'
            '"0.0","0.0","0.0","0",""', ],
        'status_code': 200, },
    {
        'name': "Un-ignore a site snag",
        'path': '/chellow/reports/373/output/',
        'method': 'post',
        'data': {
            'site_snag_id': "36",
            'ignore': "false", },
        'status_code': 303, },
    {
        'name': "Insert a batch with general import",
        'path': '/chellow/reports/293/output/',
        'method': 'post',
        'files': {'import_file': 'gi_batch.csv'},
        'status_code': 303,
        'regexes': [
            r"/reports/295/output/\?process_id=0", ], },
    {
        'path': '/chellow/reports/295/output/?process_id=0',
        'tries': {'max': 10, 'period': 1},
        'status_code': 200,
        'regexes': [
            r"The file has been imported successfully\.", ], },

    # Import some hh Stark DF2 data },
    {
        'name': "Check df2 clock change",
        'path': '/chellow/reports/211/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "53", },
        'files': {'import_file': 'hh_clock_change.df2'},
        'status_code': 303,
        'regexes': [
            r"/reports/65/output/\?hhdc_contract_id=53&process_id=0", ], },
    {
        'path': '/chellow/reports/65/output/?hhdc_contract_id=53&process_id=0',
        'tries': {'max': 10, 'period': 1},
        'regexes': [
            r"The import has completed.*successfully.", ],
        'status_code': 200, },
    {
        'path': '/chellow/reports/17/output/?supply_id=5&months=1&'
        'finish_year=2014&finish_month=03',
        'regexes': [
            r"<tr>\s*<td>\s*2014-03-30 00:30\s*</td>\s*<td>0</td>\s*"
            "<td>A</td>", ],
        'status_code': 200, },

    # Supplier contract 56

    # Create a new batch },
    {
        'name': "NHH bill outside supply period.",
        'path': '/chellow/reports/287/output/',
        'method': 'post',
        'data': {
            'supplier_contract_id': "59",
            'reference': "06-078",
            'description': "Way out batch", },
        'status_code': 303,
        'regexes': [
            r"/reports/91/output/\?supplier_batch_id=12", ], },
    {
        'path': '/chellow/reports/321/output/',
        'method': 'post',
        'data': {
            'supplier_batch_id': "12", },
        'files': {'import_file': 'nhh_bills2007.csv'},
        'status_code': 303,
        'regexes': [
            r"/reports/323/output/\?importer_id=1", ], },

    # Supplier contract 59, batch 12
    {
        'path': '/chellow/reports/323/output/?importer_id=1',
        'tries': {'max': 10, 'period': 1},
        'status_code': 200,
        'regexes': [
            r"All the bills have been successfully loaded and attached to "
            "the batch\.", ], },
    {
        'path': '/chellow/reports/219/output/?supply_id=7&months=1&'
        'end_year=2002&end_month=1',
        'status_code': 200,
        'regexes': [
            r'"2002-01-01 00:00","2002-01-31 23:30","7","22 4862 4512 332","",'
            '"06-078","20","jg87593jfj","2002-02-02 00:00","N","15","00001",'
            '"1","2002-01-04 23:30","2286","E","2002-01-06 23:30","2927",'
            '"E"', ], },

    # Attach another site to an era. Supply 2 },
    {
        'name': "Check the 'also supplies' field of a site.",
        'path': '/chellow/reports/307/output/',
        'method': 'post',
        'data': {
            'era_id': "8",
            'site_code': "CI005",
            'attach': "Attach", },
        'status_code': 303, },
    {
        'path': '/chellow/reports/5/output/?site_id=1',
        'regexes': [
            r'3475 1614 211\s*</td>\s*<td>\s*this site\s*</td>\s*<td>\s*'
            '<a href="/chellow/reports/5/output/\?site_id=3" title="Wheal '
            'Rodney">CI005</a>\s*</td>', ],
        'status_code': 200, },
    {
        'name': "In supplies snapshot, test the last billed date of MOP and "
        "DC bills",
        'path': '/chellow/reports/33/output/?supply_id=5&year=2014&month=05&'
        'day=31&hour=23&minute=30',
        'status_code': 200,
        'regexes': [
            r'"2014-05-31 23:30","CI005","Wheal Rodney","","","5","gen",'
            '"chp","22","LV","hh","no","00","845","5","","","MOP Contract",'
            '"22 0883 6932 301","HH contract","22 0883 6932 301","",'
            '"2002-01-01 00:00","hh","","2007-10-31 23:30","2007-10-31 23:30",'
            '"true","true","false","false","false","true","22 0883 6932 301",'
            '"350","570","PC 5-8 & HH LV","Half-hourlies 2013","4341","0","",'
            '"","","","","","","",""', ], },
    {
        'name': "Site summary page that has data quality errors.",
        'path': '/chellow/reports/13/output/?site_id=1&finish_year=2005&'
        'finish_month=11',
        'regexes': [
            r'See <a href="/chellow/reports/11/output/\?site_id=1&amp;'
            'months=1&amp;finish_year=2005&amp;finish_month=10">generation '
            'graph</a>', ], },
    {
        'name': "HTML virtual bill",
        'path': '/chellow/reports/101/output/?supply_id=10&start_year=2014&'
        'start_month=05&start_day=1&start_hour=0&start_minute=0&'
        'finish_year=2014&finish_month=05&finish_day=31&finish_hour=23&'
        'finish_minute=30',
        'status_code': 200, },

    {
        'name': "HTML virtual bill that spans 3 eras",
        'path': '/chellow/reports/101/output/?supply_id=2&start_year=2005&'
        'start_month=05&start_day=1&start_hour=0&start_minute=0&'
        'finish_year=2006&finish_month=07&finish_day=31&finish_hour=23&'
        'finish_minute=30',
        'status_code': 200},

    {
        'name': "Make sure rate scripts remain contiguous.",
        'path': '/chellow/reports/273/output/',
        'method': 'post',
        'data': {
            'rate_script_id': "239",

            # First rate script of non-core contract triad
            'start_year': "2005",
            'start_month': "04",
            'start_day': "01",
            'start_hour': "00",
            'start_minute': "00",
            'has_finished': "true",
            'finish_year': "2006",
            'finish_month': "03",
            'finish_day': "30",
            'finish_hour': "23",
            'finish_minute': "30",
            'script': "", },
        'status_code': 303, },
    {
        'path': '/chellow/reports/271/output/?rate_script_id=240',
        'regexes': [
            r"2006-03-31 00:00", ],
        'status_code': 200, },

    # Put it back to how it was
    {
        'path': '/chellow/reports/273/output/',
        'method': 'post',
        'data': {
            'rate_script_id': "239",
            'start_year': "2005",
            'start_month': "04",
            'start_day': "01",
            'start_hour': "00",
            'start_minute': "00",
            'has_finished': "true",
            'finish_year': "2006",
            'finish_month': "03",
            'finish_day': "31",
            'finish_hour': "23",
            'finish_minute': "30",
            'script': "", },
        'status_code': 303, },
    {
        'name': "Try sites monthly duration with displaced bill",
        'path': '/chellow/reports/161/output/?site_id=1&months=1&'
        'finish_year=2010&finish_month=07',
        'status_code': 303, },
    {
        'path': '/chellow/reports/251/output/',
        'tries': {'max': 20, 'period': 1},
        'status_code': 200,
        'regexes': [
            r"FINISHED_site_monthly_duration_for_CI004_1_to_2010_7\.csv", ], },
    {
        'path': '/chellow/reports/253/output/?'
        'name=FINISHED_site_monthly_duration_for_CI004_1_to_2010_7.csv',
        'status_code': 200,
        'regexes': [
            r'"CI004",', ], },
    {
        'name': "Try sites monthly duration covering bills",
        'path': '/chellow/reports/161/output/?site_id=4&months=1&'
        'finish_year=2011&finish_month=05',
        'status_code': 303, },
    {
        'path': '/chellow/reports/251/output/',
        'tries': {'max': 20, 'period': 1},
        'status_code': 200,
        'regexes': [
            r"FINISHED_site_monthly_duration_for_CI017_1_to_2011_5\.csv", ], },
    {
        'path': '/chellow/reports/253/output/?'
        'name=FINISHED_site_monthly_duration_for_CI017_1_to_2011_5.csv',
        'status_code': 200,
        'regexes': [
            r'"CI017",', ], },
    {
        'name': "Try sites monthly duration with a clocked bill",
        'path': '/chellow/reports/321/output/',
        'method': 'post',
        'data': {
            'supplier_batch_id': "7", },
        'files': {'import_file': 'bills-nhh-clocked.csv'},
        'status_code': 303, },
    {
        'path': '/chellow/reports/161/output/?site_id=4&months=1&'
        'finish_year=2012&finish_month=02',
        'status_code': 303, },
    {
        'path': '/chellow/reports/251/output/',
        'tries': {'max': 20, 'period': 1},
        'status_code': 200,
        'regexes': [
            r"FINISHED_site_monthly_duration_for_CI017_1_to_2012_2\.csv", ], },
    {
        'path': '/chellow/reports/253/output/?'
        'name=FINISHED_site_monthly_duration_for_CI017_1_to_2012_2.csv',
        'status_code': 200,
        'regexes': [
            r'"CI017",', ], },

    # Bill check on a clocked bill
    {
        'path': '/chellow/reports/111/output/?bill_id=21',
        'status_code': 200,
        'regexes': [
            r'"07-002","3423760010","N","10","9.07","0.21","2012-01-05 00:00",'
            '"2012-01-10 23:30","22 1065 3921 534","CI017","Roselands",'
            '"2012-01-05 00:00","2012-01-10 23:30","21","9.07","1.0","8.07",'
            '"10.0","10.0","",', ], },
    {
        'name': "Monthly supplies duration with export hh data",
        'path': '/chellow/reports/177/output/?supply_id=1&months=1&'
        'end_year=2008&end_month=07',
        'status_code': 303, },
    {
        'path': '/chellow/reports/251/output/',
        'tries': {'max': 10, 'period': 1},
        'status_code': 200,
        'regexes': [
            r"FINISHED_supplies_monthly_duration_for_1_1_to_2008_7\.csv", ], },
    {
        'path': '/chellow/reports/253/output/?'
        'name=FINISHED_supplies_monthly_duration_for_1_1_to_2008_7.csv',
        'status_code': 200,
        'regexes': [
            r"supply-id,supply-name,source-code,generator-type,month,pc-code,"
            "msn,site-code,site-name,metering-type,import-mpan-core,"
            "metered-import-kwh,metered-import-net-gbp,"
            "metered-import-estimated-kwh,billed-import-kwh,"
            "billed-import-net-gbp,export-mpan-core,metered-export-kwh,"
            "metered-export-estimated-kwh,billed-export-kwh,"
            "billed-export-net-gbp,problem,timestamp",
            r'1,"Hello","sub","","2008-07-31 23:30","00","","CH017","Parbola",'
            '"hh","None","18.281","0","0","0","0","22 0470 7514 535","0","0",'
            '"0","0",""', ], },

    # Supply level hh data CSV, hh per row
    {
        'name': "Supply level hh data CSV, hh per row",
        'path': '/chellow/reports/187/output/',
        'method': 'post',
        'data': {
            'supply_id': '7', 'start_year': '2008', 'start_month': '01',
            'start_day': '01', 'start_hour': '0', 'start_minute': '0',
            'finish_year': '2008', 'finish_month': '01', 'finish_day': '31',
            'finish_hour': '23', 'finish_minute': '30'},
        'status_code': 303},
    {
        'path': '/chellow/reports/251/output/',
        'tries': {'max': 10, 'period': 1},
        'status_code': 200,
        'regexes': [
            r"FINISHED_hh_data_row_200801010000\.csv", ], },
    {
        'path': '/chellow/reports/253/output/?'
        'name=FINISHED_hh_data_row_200801010000.csv',
        'status_code': 200,
        'regexes': [
            r'"CH023","22 4862 4512 332","","2008-01-01 00:00","3.77","A","",'
            '"","","","","","","","",""']},

    {
        'name': "Supply level hh data CSV, hh per row. MPAN core filter.",
        'path': '/chellow/reports/187/output/',
        'method': 'post',
        'data': {
            'start_year': '2010', 'start_month': '01', 'start_day': '01',
            'start_hour': '0', 'start_minute': '0', 'finish_year': '2010',
            'finish_month': '12', 'finish_day': '31', 'finish_hour': '23',
            'finish_minute': '30', 'mpan_cores': '22 4862 4512 332'},
        'status_code': 303},
    {
        'path': '/chellow/reports/251/output/',
        'tries': {'max': 10, 'period': 1},
        'status_code': 200,
        'regexes': [
            r"FINISHED_hh_data_row_201001010000\.csv", ], },
    {
        'path': '/chellow/reports/253/output/?'
        'name=FINISHED_hh_data_row_201001010000.csv',
        'status_code': 200,
        'regexes': [
            r'"Export REACTIVE_EXP Status"\s'
            r'"CH023","22 4862 4512 332","","2010-02-04 20:00","30.4339","A",'
            r'"","","","","","","","","",""']},

    {
        'name': "General import of bill with start date after finish date",
        'path': '/chellow/reports/293/output/',
        'method': 'post',
        'files': {'import_file': 'general-bills-error.csv'},
        'status_code': 303,
        'regexes': [
            r"/reports/295/output/\?process_id=1", ], },
    {
        'path': '/chellow/reports/295/output/?process_id=1',
        'tries': {'max': 10, 'period': 1},

        # Check good error message
        'regexes': [
            r"The bill start date 2007-01-05 00:00 can&#39;t be after the "
            "finish date 2007-01-01 00:00.", ],
        'status_code': 200, },
    {
        'name': "Manually insert a bill with errors",
        'path': '/chellow/reports/313/output/',
        'method': 'post',
        'data': {
            'supplier_batch_id': "4",
            'mpan_core': "",
            'reference': "",
            'issue_year': "2014",
            'issue_month': "7",
            'issue_day': "30",
            'issue_hour': "15",
            'issue_minute': "30",
            'start_year': "2014",
            'start_month': "07",
            'start_day': "30",
            'start_hour': "15",
            'start_minute': "30",
            'finish_year': "2014",
            'finish_month': "07",
            'finish_day': "30",
            'finish_hour': "15",
            'finish_minute': "30",
            'kwh': "0",
            'net': "0",
            'vat': "0",
            'gross': "0",
            'account': "0",
            'bill_type_id': "1",
            'breakdown': "{}", },
        'status_code': 400,

        # Check good error message
        'regexes': [
            r"The MPAN core &#39;&#39; must contain exactly 13 digits\.", ], },

    # Must straddle two eras },
    {
        'name': "HH by HH virtual bill",
        'path': '/chellow/reports/387/output/?supply_id=5&start_year=2012&'
        'start_month=12&start_day=31&start_hour=23&start_minute=30&'
        'finish_year=2013&finish_month=1&finish_day=1&finish_hour=23&'
        'finish_minute=30',
        'status_code': 200,
        'regexes': [
            r"supply_virtual_bills_hh_5.csv",
            r'"22 0883 6932 301",', ], },

    # Add in reactive HH },
    {
        'name': "Look at monthly report with an MD in kVA",
        'path': '/chellow/reports/303/output/',
        'method': 'post',
        'data': {
            'channel_id': "55",
            'start_year': "2010",
            'start_month': "02",
            'start_day': "04",
            'start_hour': "20",
            'start_minute': "00",
            'insert': "Insert",
            'value': "45.7",
            'status': "A", },
        'status_code': 303, },
    {
        'path': '/chellow/reports/15/output/?is_import=true&supply_id=7&'
        'years=1&year=2010',
        'status_code': 200,
        'regexes': [
            r"<tr>\s*<td>2010-02-01 00:00</td>\s*<td>22 4862 4512 332</td>\s*"
            "<td>\s*2010-02-04 20:00\s*</td>\s*<td>60.9</td>\s*"
            "<td>91.4</td>\s*<td>0.55</td>\s*<td>109.8</td>\s*<td>230</td>\s*"
            "<td>\s*30\s*</td>\s*</tr>", ], },

    # Add in second batch },
    {
        'name': "Order of HHDC batches",
        'path': '/chellow/reports/281/output/',
        'method': 'post',
        'data': {
            'hhdc_contract_id': "53",
            'reference': "7",
            'description': "", },
        'status_code': 303, },
    {
        'path': '/chellow/reports/93/output/?hhdc_contract_id=53',
        'status_code': 200,
        'regexes': [
            r'<tr>\s*<td>\s*'
            '<a href="/chellow/reports/203/output/\?hhdc_batch_id=13">\s*7\s*'
            '</a>\s*</td>\s*<td></td>\s*</tr>\s*<tr>\s*<td>\s*'
            '<a href="/chellow/reports/203/output/\?hhdc_batch_id=8">\s*'
            '001-7t\s*</a>\s*</td>\s*<td>hhdc batch</td>\s*</tr>', ], },

    # Add in second batch },
    {
        'name': "Order of MOP batches",
        'path': '/chellow/reports/353/output/',
        'method': 'post',
        'data': {
            'mop_contract_id': "57",
            'reference': "7a",
            'description': "", },
        'status_code': 303, },
    {
        'path': '/chellow/reports/191/output/?mop_contract_id=57',
        'status_code': 200,
        'regexes': [
            r'<tr>\s*<td>\s*'
            '<a href="/chellow/reports/193/output/\?mop_batch_id=9">\s*'
            '99/992\s*</a>\s*</td>\s*<td>mop batch</td>\s*</tr>\s*<tr>\s*'
            '<td>\s*'
            '<a href="/chellow/reports/193/output/\?mop_batch_id=14">\s*7a\s*'
            '</a>\s*</td>\s*<td></td>\s*</tr>', ], },

    {
        'name': "MTCs",
        'path': '/chellow/reports/61/output/',
        'status_code': 200,
        'regexes': [
            r'<tr>\s*<td>\s*'
            '<a href="/chellow/reports/63/output/\?mtc_id=574">\s*001\s*'
            '</a>\s*</td>\s*<td>\s*'
            '<a href="/chellow/reports/67/output/\?dno_contract_id=39">\s*'
            '12\s*</a>\s*</td>\s*<td>Economy 7, 23.30 - 06.30</td>\s*<td>\s*'
            '<a href="/chellow/reports/131/output/\?meter_type_id=15">\s*TP\s*'
            '</a>\s*</td>\s*<td>2</td>\s*</tr>', ], },

    {
        'path': '/chellow/reports/63/output/?mtc_id=574',
        'status_code': 200,
        'regexes': [
            r'<tr>\s*<th>Code</th>\s*<td>001</td>\s*</tr>\s*<tr>\s*'
            '<th>DNO</th>\s*<td>\s*'
            '<a href="/chellow/reports/67/output/\?dno_contract_id=39">\s*'
            '12\s*</a>\s*</td>\s*</tr>', ], },

    # Try an MTC common to all DNOs
    {
        'path': '/chellow/reports/63/output/?mtc_id=233',
        'status_code': 200,
        'regexes': [
            r"<tr>\s*<th>Code</th>\s*<td>500</td>\s*</tr>\s*<tr>\s*"
            "<th>DNO</th>\s*<td>\s*All\s*</td>\s*</tr>", ], },
    {
        'name': "Move forward era with channels, when era with no channels "
        "precedes it",
        'path': '/chellow/reports/299/output/',
        'method': 'post',
        'data': {
            'era_id': "17",
            'imp_related': "true",
            'channel_type': "ACTIVE", },
        'status_code': 303, },
    {
        'path': '/chellow/reports/307/output/',
        'method': 'post',
        'data': {
            'era_id': "17",
            'msn': "I02D89150",
            'start_year': "2010",
            'start_month': "01",
            'start_day': "06",
            'start_hour': "00",
            'start_minute': "00",
            'is_ended': "false",
            'mop_contract_id': "57",
            'mop_account': "mc-22 1065 3921 534",
            'hhdc_contract_id': "53",
            'hhdc_account': "dc-22 1065 3921 534",
            'pc_id': "3",
            'mtc_code': "801",
            'cop_id': "6",
            'ssc_code': "366",
            'imp_llfc_code': "110",
            'imp_mpan_core': "22 1065 3921 534",
            'imp_sc': "30",
            'imp_supplier_contract_id': "63",
            'imp_supplier_account': "SA342376000", },
        'status_code': 303, },

    # Add new era, so that bill straddles join },
    {
        'name': "NHH dumb bill that straddles dumb and AMR eras",
        'path': '/chellow/reports/305/output/',
        'method': 'post',
        'data': {
            'supply_id': "11",
            'start_year': "2007",
            'start_month': "07",
            'start_day': "10",
            'start_hour': "00",
            'start_minute': "00",
            'insert_era': "Insert", },
        'regexes': [
            r"/chellow/reports/7/output/\?supply_id=11", ],
        'status_code': 303, },

    # Add a channel to the new era
    {
        'path': '/chellow/reports/299/output/',
        'method': 'post',
        'data': {
            'era_id': "27",
            'imp_related': "true",
            'channel_type': "ACTIVE", },
        'status_code': 303, },
    {
        'path': '/chellow/reports/111/output/?bill_id=6',
        'status_code': 200,
        'regexes': [
            r'"06-002","23618619","N","0","49119","8596","2007-06-30 00:00",'
            '"2007-07-31 00:00","22 9974 3438 105","CI005","Wheal Rodney",'
            '"2007-06-30 00:00","2007-07-31 00:00","6","49119.0","0.0",'
            '"49119.0","8596.0","0.0","8596.0","","0.0","","0.0","4.765","",'
            '""', ], },
    {
        'name': "NHH dumb bill with prev and pres dates in different eras",
        'path': '/chellow/reports/307/output/',
        'method': 'post',
        'data': {
            'era_id': "10",
            'start_year': "2005",
            'start_month': "09",
            'start_day': "06",
            'start_hour': "00",
            'start_minute': "00",
            'is_ended': "true",
            'finish_year': "2011",
            'finish_month': "01",
            'finish_day': "19",
            'finish_hour': "23",
            'finish_minute': "30",
            'mop_contract_id': "57",
            'mop_account': "mc-22 1065 3921 534",
            'hhdc_contract_id': "54",
            'hhdc_account': "dc-22 1065 3921 534",
            'msn': "I02D89150",
            'pc_id': "3",
            'mtc_code': "801",
            'cop_id': "5",
            'ssc_code': "0393",
            'imp_llfc_code': "110",
            'imp_mpan_core': "22 1065 3921 534",
            'imp_sc': "30",
            'imp_supplier_contract_id': "63",
            'imp_supplier_account': "SA342376", },
        'status_code': 303, },

    # Check the bill
    {
        'path': '/chellow/reports/111/output/?bill_id=13',
        'status_code': 200,
        'regexes': [
            r'"07-002","3423760005","N","150","98.17","15.01",'
            '"2011-01-05 00:00","2011-01-10 23:30","22 1065 3921 534",'
            '"CI017","Roselands","2011-01-05 00:00","2011-01-10 23:30","13",'
            '"98.17","164.1","-65.93","150.0","1641.0","",""', ], },

    # Update register read to make the TPR a teleswitch one },
    {
        'name': "Check bill with teleswitch TPR",
        'path': '/chellow/reports/31/output/',
        'method': 'post',
        'data': {
            'supplier_read_id': "16",
            'mpan': "22 1065 3921 534",
            'coefficient': "1",
            'msn': "I02D89150",
            'units': "kWh",
            'tpr_id': "643",
            'previous_year': "2012",
            'previous_month': "01",
            'previous_day': "04",
            'previous_hour': "23",
            'previous_minute': "30",
            'previous_value': "473",
            'previous_type_id': "1",
            'present_year': "2012",
            'present_month': "01",
            'present_day': "06",
            'present_hour': "23",
            'present_minute': "30",
            'present_value': "725",
            'present_type_id': "1",
            'update': "Update", },
        'status_code': 303, },

    # Delete the channel to make it a dumb NHH
    {
        'path': '/chellow/reports/303/output/',
        'method': 'post',
        'data': {
            'channel_id': "56",
            'delete': "delete", },
        'status_code': 303, },

    # Check the bill
    {
        'path': '/chellow/reports/111/output/?bill_id=21',
        'status_code': 200,
        'regexes': [
            r'"07-002","3423760010","N","10","9.07","0.21","2012-01-05 00:00",'
            '"2012-01-10 23:30","22 1065 3921 534","CI017","Roselands",'
            '"2012-01-05 00:00","2012-01-10 23:30","21","9.07","0.0","9.07",'
            '"10.0","0","",""', ], },

    # Update register read to make the TPR a teleswitch one },
    {
        'name': "CRC with read pair straddling eras",
        'path': '/chellow/reports/31/output/',
        'method': 'post',
        'data': {
            'supplier_read_id': "7",
            'mpan': "22 1065 3921 534",
            'coefficient': "1",
            'msn': "I02D89150",
            'units': "kWh",
            'tpr_id': "1",
            'previous_year': "2009",
            'previous_month': "04",
            'previous_day': "04",
            'previous_hour': "23",
            'previous_minute': "30",
            'previous_value': "14281",
            'previous_type_id': "1",
            'present_year': "2010",
            'present_month': "01",
            'present_day': "06",
            'present_hour': "23",
            'present_minute': "30",
            'present_value': "15924",
            'present_type_id': "1",
            'update': "Update", },
        'status_code': 303, },
    {
        'path': '/chellow/reports/207/output/?supply_id=10&year=2009',
        'status_code': 200,
        'regexes': [
            r'"10","22 1065 3921 534","CI017","Roselands","2009-04-01 00:00",'
            '"2010-03-31 23:30",".*?","0","0","277.0","0","0","0","365.0","0",'
            '"277.0","365.0","Actual","0","0","1666.72563177","0",'
            '"1666.72563177"', ], },

    # Add a scenario },
    {
        'name': "Run a BAU scenario",
        'path': '/chellow/reports/315/output/',
        'method': 'post',
        'data': {
            'participant_id': "54",  # COOP
            'name': "scenario_bau",
            'start_year': "2000",
            'start_month': "01",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00",
            'charge_script': "",
            'properties': """
{
    'bsuos' : {
        'start_date': None,  # Date or None for latest rate script
        'multiplier': 1.5,
        'constant': 0,
    },

    'ccl': {
        'start_date': datetime(2014, 10, 1),
        'multiplier': 1,
        'constant': 0,
    },

    'aahedc': {
        'start_date': None,
        'multiplier': 0,
        'constant': 0.00091361,
    },

    'scenario_start': None,  # Date or None for this month
    'scenario_duration': 1,  # Number of months

    'kw_changes':

    # MPAN Core, Date, kW
    '''
    ''',
}
""", },
        'regexes': [
            r"/reports/77/output/\?supplier_contract_id=64", ],
        'status_code': 303, },

    # Run scenario for a site where there are no site groups
    {
        'path': '/chellow/reports/247/output/?site_id=1&scenario_id=64',
        'status_code': 200,

        # Check file name is correct
        'regexes': [
            r"'content-disposition', 'attachment; "
            'filename="scenario_\d{12}.csv"'
            "'",
            r"exp-supplier-problem$", ], },

    # Run scenario for a site where there are site groups
    {
        'path': '/chellow/reports/247/output/?site_id=3&scenario_id=64',
        'status_code': 200,
        'regexes': [
            r"CI005", ], },
    {
        'name': "Check BSUoS automatic import page",
        'path': '/chellow/reports/227/output/',
        'status_code': 200,
        'regexes': [
            r"Is Locked\?", ], },
    {
        'name': "Check RCRC automatic import page",
        'path': '/chellow/reports/225/output/',
        'status_code': 200,
        'regexes': [
            r"Is Locked\?", ], },
    {
        'name': "Check TLM automatic import page",
        'path': '/chellow/reports/223/output/',
        'status_code': 200,
        'regexes': [
            r"Is Locked\?", ], },

    # Add a scenario },
    {
        'name': "Run an increased BSUoS scenario",
        'path': '/chellow/reports/315/output/',
        'method': 'post',
        'data': {
            'participant_id': "54",  # COOP
            'name': "scenario_bsuos",
            'start_year': "2000",
            'start_month': "01",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00",
            'charge_script': "",
            'properties': """
{
    'bsuos' : {
        'start_date': datetime(2011, 1, 1),
        'multiplier': 1,
        'constant': 0.1,
    },

    'ccl': {
        'start_date': datetime(2014, 10, 1),
        'multiplier': 1,
        'constant': 0,
    },

    'aahedc': {
        'start_date': datetime(2011, 1, 1),
        'multiplier': 1,
        'constant': 0.1,
    },

    'scenario_start': datetime(2011, 1, 1),  # Date or None for this month
    'scenario_duration': 1,  # Number of months
    'resolution': 'hh',  # 'hh' or 'month'

    'kw_changes':

    # MPAN Core, Date, kW
    '''
    ''',
}
""", },
        'regexes': [
            r"/reports/77/output/\?supplier_contract_id=65", ],
        'status_code': 303, },

    # Run scenario for a site
    {
        'path': '/chellow/reports/247/output/?site_id=3&scenario_id=65',
        'status_code': 200,
        'regexes': [
            r'"22 6158 2968 220","22 3479 7618 470","net","CI005",'
            '"Wheal Rodney","2011-01-31 23:30","0","0","0","0","0","0","0",'
            '"0","0","179.2268","0","0","0","0","0","0","179.2268","0","","0",'
            '"","","0","","","179.2268","","","0.0047","","5.89",'
            '"130","31","0.0163","65.689","0","31","0.0163","0.0","","","","",'
            '"0.00202","0.0","","88","0","0.0","0.0","0","0.0","0.0","","","",'
            '"","",'
            '"","0","0.0","0.0","0","0.0","0.0","0.0","","0.0","",'
            '"","","","","",'
            '"","","","","","","","","","","","","2010-01-07 17:00","0","X",'
            '"1.058","0.0","2010-01-25 17:00","0","X","1.058","0.0",'
            '"2009-12-15 17:00","0","X","1.058","0.0","0.0","24.031029","1",'
            '"0.0","","","","0","0.00052","0.0","0.0","0","0.11678","0.0",'
            '"0.0",'
            '"31",'
            '"0.6338","19.6478","0","0.0","0.10016297","0.0","0.0",'
            '"","0.0","","","","","112.0808","","",'
            '"0.0047","","5.89","20","31","0.0163","10.106","0","31","0.0",'
            '"0.0","","","","","0.00106","0.0","","88","0","0.0","0.0","0",'
            '"0.0","0.0","0","0","0.0","0","0","0.0","0","0.0","0.0","0",'
            '"0.0",'
            '"0.0","0.0","","0.0","","","","","","","","","","","",'
            '"","","","","","","","2010-01-07 17:00","0","X","1.058","0.0",'
            '"2010-01-25 17:00","0","X","1.058","0.0","2009-12-15 17:00","0",'
            '"X","1.058","0.0","0.0","24.031029","1","0.0","","",""']},

    # Add a scenario
    {
        'name': "Run a used and generated scenario",
        'path': '/chellow/reports/315/output/',
        'method': 'post',
        'data': {
            'participant_id': "54",  # COOP
            'name': "scenario_used",
            'start_year': "2000",
            'start_month': "01",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00",
            'charge_script': "",
            'properties': r"""
{
    'bsuos' : {
        'start_date': datetime(2011, 1, 1),
        'multiplier': 1,
        'constant': 0,
    },

    'ccl': {
        'start_date': datetime(2014, 10, 1),
        'multiplier': 1,
        'constant': 0,
    },

    'aahedc': {
        'start_date': None,
        'multiplier': 0,
        'constant': 0.00091361,
    },

    'scenario_start': datetime(2011, 1, 1),  # Date or None for this month
    'scenario_duration': 1,  # Number of months
    'resolution': 'hh',  # 'hh' or 'month'

    'kw_changes':
    # CSV format with the following columns
    # Site Code, Type ('used' or 'generated') , Date (yyyy-mm-dd), Multiplier
    "CI005, used, 2011-01-01, 0.5\nCI005, generated, 2011-01-01, 2"}
""", },
        'regexes': [
            r"/reports/77/output/\?supplier_contract_id=66", ],
        'status_code': 303, },

    # Run scenario for a site
    {
        'path': '/chellow/reports/247/output/?site_id=3&scenario_id=66',
        'status_code': 200,
        'regexes': [
            r'"22 0195 4836 192","None","net","CI005","Wheal Rodney",'
            '"2011-01-31 23:30","12.9095890411","0","0","0","0","0","0",'
            '"12.9095890411","0","0.0","0","0","0","0","0","0","0.0","0","",'
            '"0","","","0","","","0.0","","","","","","","","","","","","","",'
            '"","","","","","","","","","","","","","","","","","","","","",'
            '"","","","","","","","","","","","","","","","","","","","","",'
            '"","","","","","","","","","","","","","","","","","","","","",'
            '"","","","","","","","","","","","","","","","","","","","","",'
            '"","","","0.0","0.0","12.9095890411"', ], },

    # Try to detach an era from its physical site
    {
        'name': "Detach an era",
        'path': '/chellow/reports/307/output/',
        'method': 'post',
        'data': {
            'era_id': "8",
            'site_id': "1",
            'detach': "Detach", },
        'status_code': 400,
        'regexes': [
            r"<li>You can&#39;t detach an era from the site where it is "
            "physically located.</li>", ], },
    {
        'name': "Look at a DNO",
        'path': '/chellow/reports/67/output/?dno_contract_id=38',
        'status_code': 200, },
    {
        'name': "Look at the SSCs",
        'path': '/chellow/reports/125/output/',
        'status_code': 200, },
    {
        'name': "Rate start after last rate scripts",
        'path': '/chellow/reports/317/output/',
        'method': 'post',
        'data': {
            'supplier_contract_id': "65",
            'party_id': "90",  # COOP
            'name': "scenario_bsuos",
            'start_year': "2000",
            'start_month': "01",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00",
            'charge_script': "",
            'properties': """
{
    'bsuos' : {
        'start_date': datetime(5010, 1, 1),
        'multiplier': 1,
        'constant': 0.1,
    },

    'ccl': {
        'start_date': datetime(2014, 10, 1),
        'multiplier': 1,
        'constant': 0,
    },

    'aahedc': {
        'start_date': datetime(2011, 1, 1),
        'multiplier': 1,
        'constant': 0.1,
    },

    'scenario_start': datetime(5011, 1, 1),  # Date or None for this month
    'scenario_duration': 1,  # Number of months
    'resolution': 'hh',  # 'hh' or 'month'

    'kw_changes':

    # MPAN Core, Date, kW
    '''
    ''',
}
""", },
        'regexes': [
            r"/reports/77/output/\?supplier_contract_id=65", ],
        'status_code': 303, },

    # Run scenario for a site
    {
        'path': '/chellow/reports/247/output/?site_id=3&scenario_id=65',
        'status_code': 200,
        'regexes': [
            r'"22 6158 2968 220","22 3479 7618 470","net","CI005",'
            '"Wheal Rodney","5011-01-31 23:30","0","0","0","0","0","0","0",'
            '"0","0","206.5347","0","0","0","0","0","0","206.5347","0","","0",'
            '"","","0","","","206.5347","","","0.00525288","","5.89",'
            '"130","31","0.0229","92.287","0","31","0.0229","0.0","","","","",'
            '"0.0026","0.0","","88","0","0.0","0.0","0","0.0","0.0","","","",'
            '"","",'
            '"","0","0.0","0.0","0","0.0","0.0","0.0","","0.0","","","","",'
            '"","",'
            '"","","","","","","","","","","","","2014-11-25 17:00","0","X",'
            '"1.065","0.0","2014-12-06 17:00","0","X","1.05","0.0",'
            '"2015-01-30 17:00","0","X","1.065","0.0","0.0","37.42","1","0.0",'
            '"","","","0","0.00066","0.0","0.0","0","0.19574","0.0","0.0",'
            '"31","0.6567",'
            '"20.3577","0","0.0","0.10016297","0.0","0.0",'
            '"","0.0","","","","","103.8937","","",'
            '"0.00525288","","5.89","20","31","0","0","0","31","0","0","","",'
            '"","","0.00095","0.0","","88","0","0.0","0.0","0","0.0","0.0",'
            '"0",'
            '"0","0.0","0","0","0.0","0","0.0","0.0","0","0.0","0.0","0.0",'
            '"","0.0","","","","","","","","","","","","","","","",'
            '"","","","2014-11-25 17:00","0","X","1.065","0.0",'
            '"2014-12-06 17:00","0","X","1.05","0.0","2015-01-30 17:00","0",'
            '"X","1.065","0.0","0.0","37.42","1","0.0","","",""']},
    {
        'name': "Show edit channel snag",
        'path': '/chellow/reports/365/output/?snag_id=100',
        'status_code': 200, },

    # GI Delete LLFC
    {
        'name': "GI Delete LLFC",
        'path': "/chellow/reports/293/output/",
        'method': "post",
        'files': {"import_file": "gi_delete_llfc.csv"},
        'status_code': 303,
        'regexes': [r"/reports/295/output/\?process_id=2"]},
    {
        'name': "Check import has succeeded",
        'path': "/chellow/reports/295/output/?process_id=2",
        'tries': {'max': 10, 'period': 1},
        'status_code': 200,
        'regexes': [r"The file has been imported successfully\."]},

    # MDD Converter
    {
        'name': "MDD Converter",
        'path': "/chellow/reports/163/output/",
        'method': "post",
        'files': {"file": "Line_Loss_Factor_Class_225.csv"},
        'status_code': 200,
        'regexes':  [
            '"insert","llfc","19","889","PROLOGIS, BEDDINGTON - IMPORT","LV",'
            '"False","True","1996-04-01 00:00",""']},

    # GI Insert LLFC
    {
        'name': "GI Insert LLFC",
        'path': "/chellow/reports/293/output/",
        'method': "post",
        'files': {'import_file': "gi_insert_llfc.csv"},
        'status_code': 303,
        'regexes': [
            "/reports/295/output/\?process_id=3"]},
    {
        'name': "GI Insert LLFC. Check it worked.",
        'path': "/chellow/reports/295/output/?process_id=3",
        'tries': {'max': 10, 'period': 1},
        'status_code': 200,
        'regexes': [r"The file has been imported successfully\."]},

    # CRC Selector
    {
        'name': "CRC Selector",
        'path': "/chellow/reports/209/output/",
        'status_code': 200},

    # Dumb NHH supply with DUoS pass-through
    {
        'name': "Dumb NHH supply with DUoS pass-through: "
        "Update Non half-hourlies 2010",
        'path': "/chellow/reports/317/output/",
        'method': 'post',
        'data': {
            'supplier_contract_id': '63',
            'party_id': '90',
            'name': 'Non half-hourlies 2010',
            'charge_script': """from net.sf.chellow.monad import Monad
import datetime
import pytz
from dateutil.relativedelta import relativedelta

Monad.getUtils()['impt'](globals(), 'db', 'utils', 'templater', 'duos')

def virtual_bill_titles():
        return ['net-gbp', 'sum-msp-kwh', 'problem']

def virtual_bill(supply_source):
    sum_msp_kwh = sum(h['msp-kwh'] for h in supply_source.hh_data)
    bill = supply_source.supplier_bill
    duos.duos_vb(supply_source)
    for rate_name, rate_set in supply_source.supplier_rate_sets.iteritems():
        if len(rate_set) == 1:
            bill[rate_name] = rate_set.pop()
            bill['net-gbp'] = sum_msp_kwh * 0.1
            bill['sum-msp-kwh'] = sum_msp_kwh
""",
            'properties': '{}'},
        'status_code': 303},
    {
        'name': "Dumb NHH supply with DUoS pass-through: "
        "Run virtual bill",
        'path': '/chellow/reports/291/output/?supply_id=16&start_year=2015&'
        'start_month=03&start_day=01&start_hour=00&start_minute=0&'
        'finish_year=2015&finish_month=03&finish_day=31&finish_hour=23&'
        'finish_minute=30',
        'regexes': [
            r'"Imp MPAN Core","Exp MPAN Core","Site Code","Site Name",'],
        'status_code': 200},

    # Forecast that includes a leap day
    {
        'name': "Leap day forecast. Create scenario",
        'path': '/chellow/reports/315/output/',
        'method': 'post',
        'data': {
            'participant_id': "54",  # COOP
            'name': "scenario_leap_day",
            'start_year': "2000",
            'start_month': "01",
            'start_day': "03",
            'start_hour': "00",
            'start_minute': "00",
            'charge_script': "",
            'properties': """
{
    'kwh_start': datetime(2009, 4, 1),
    'scenario_start': datetime(2016, 2, 1),  # Date or None for this month
    'scenario_duration': 1,  # Number of months
    'resolution': 'hh',  # 'hh' or 'month'

    'kw_changes':

    # MPAN Core, Date, kW
    '''
    ''',
}
""", },
        'regexes': [
            r"/reports/77/output/\?supplier_contract_id=67", ],
        'status_code': 303, },

    {
        'name': "Leap day forecast. Run scenario for a site",
        'path': '/chellow/reports/247/output/?site_id=5&scenario_id=67',
        'status_code': 200,
        'regexes': [
            r'"22 4862 4512 332","None","net","CH023","Treglisson",'
            '"2016-02-29 23:30","23562.05","0","0","0","0","0","0","23562.05",'
            '"0","0.0","0","0","0","0","0","0","0.0","0","","0","","","0","",'
            '"","0.0","","","","","","","","","","","","","","","","","","",'
            '"","","","","","","","","","","","","","","","","","","","","",'
            '"","","","","","","","","","","","","","","","","","","","","",'
            '"","","","","","","","","","","","","","","","","","","","","",'
            '"","","","","","","","","","","","","","","","","","","","0.0",'
            '"0.0","23562.05"']},

    {
        'name': "Check CSV Supplies HH Data. With mpan_cores",
        'path': '/chellow/reports/169/output/',
        'method': 'post',
        'data': {
            'mpan_cores': '22 0470 7514 535', 'imp_related': 'true',
            'channel_type': 'ACTIVE',
            'start_year': '2008', 'start_month': '7', 'start_day': '1',
            'start_hour': '0', 'start_minute': '0', 'finish_year': '2008',
            'finish_month': '08', 'finish_day': '1', 'finish_hour': '23',
            'finish_minute': '30'},
        'status_code': 303, },
    {
        'path': '/chellow/reports/251/output/',
        'tries': {'max': 20, 'period': 1},
        'status_code': 200,
        'regexes': [
            r"FINISHED_supplies_hh_data_200808013023\.csv", ], },
    {
        'path': '/chellow/reports/253/output/?'
        'name=FINISHED_supplies_hh_data_200808013023.csv',
        'status_code': 200,

        # Check the HH data is there
        'regexes': [
            r"NA,2008-07-06,0\.262", ]},
]