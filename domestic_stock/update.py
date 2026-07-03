# 노션에 쓰는 함수만 넣는다.

from config import NOTION_PRICE_DB_ID
from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할
from data.domestic_stock import give_properties
import os

def update_price:
    
    properties = give_properties()
    notion.pages.update(
        page_id=page["id"],
        properties=properties
    )
