from net.sf.chellow.monad import Monad
from sqlalchemy.orm import joinedload_all

Monad.getUtils()['imprt'](globals(), {
        'db': ['Contract', 'Party', 'RateScript', 'set_read_write', 'session'], 
        'utils': ['UserException'],
        'templater': ['render']})

sess = None
try:
    sess = session()
    mop_contracts = sess.query(Contract).from_statement("select contract.* from contract, market_role where contract.market_role_id = market_role.id and market_role.code = 'M' order by contract.name").all()
    render(inv, template, {'mop_contracts': mop_contracts})
finally:
    sess.close()