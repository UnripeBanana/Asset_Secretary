# 노션에 쓰는 함수만 넣는다.

from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할
from data.domestic_stock import get_naver_prop, get_yfinance_prop

def update_stock_DB(page, stock_info):
    notion.pages.update(
        page_id=page["id"],
        properties=stock_info
    )


###############
price_info = get_naver_price(ticker)

            current_price = price_info["price"]
            change = price_info["change"]
            upanddown = price_info["cr"]
            # 하락이면 음수로 변경
            if price_info["rf"] == "5":
                change = -change
                upanddown = -upanddown

            countOfListedStock = price_info["countOfListedStock"]

            ###################################
            
            # y_finance
            stock = yf.Ticker(f"{ticker}.KS")

            info = stock.info
            market_cap = info.get("marketCap", 0)
            
            if market_cap is None:
                market_cap = 0

            high_52 = info.get("fiftyTwoWeekHigh")
            low_52 = info.get("fiftyTwoWeekLow")

            currency = info.get("currency")
            country = info.get("country")
            sector = info.get("sector")
            industry = info.get("industry")

            update_time = datetime.now(
                ZoneInfo("Asia/Seoul")
            ).strftime("%Y-%m-%d %H:%M")

            properties = {
                "현재가_깃허브_원본": {
                    "number": current_price
                },
                "전일대비_깃허브": {
                    "number": change
                },
                "등락률_깃허브_원본": {
                    "number": upanddown
                },
                "시가총액_깃허브": {
                    "number": countOfListedStock*current_price
                },
                "52주 최고가": {
                    "number": high_52
                },
                "52주 최저가": {
                    "number": low_52
                },
                "통화": rich_text(currency),
                "국가": rich_text(country),
                "업종": rich_text(sector),
                "산업": rich_text(industry),
                "마지막 업데이트": rich_text(update_time)
            }
