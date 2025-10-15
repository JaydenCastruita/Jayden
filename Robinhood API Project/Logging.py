import robin_stocks.robinhood as r
from GetPassword import get_password

def login_to_robinhood():
    email, password = get_password()
    r.login(email, password)
    return r.build_holdings()