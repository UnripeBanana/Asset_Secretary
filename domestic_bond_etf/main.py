from datetime import datetime
from zoneinfo import ZoneInfo
from domestic_bond_etf.read import get_ticker
from domestic_bond_etf.update import update_bond_etf_DB
from data.domestic_bond_etf import get_naver_prop
from history.history import append_prices

def domestic_bond_etf_DB_main(pages):
    for page in pages:
        ticker = get_ticker(page)
        if not ticker:
            continue

        stock_info = get_naver_prop(ticker)

        update_bond_etf_DB(page, stock_info)
