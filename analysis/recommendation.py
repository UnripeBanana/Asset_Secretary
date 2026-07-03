# 리밸런싱 결과를 토대로 사용자에게 전달할 피드백 생성

from config import NOTION_TOKEN, NOTION_PRICE_DB_ID, NOTION_TRADE_DB_ID
from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할
