from config import NOTION_PRICE_DB_ID
from notion.get_all_pages import get_all_pages
from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할
from domestic_stock.read import get_ticker
from domestic_stock.update import update_stock_DB

for page in get_all_pages(NOTION_PRICE_DB_ID):

  ticker = get_ticker(page)
  
  stock_info = {
      **get_naver_prop(ticker),
      **get_yfinance_prop(ticker)
  }

  
