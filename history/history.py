import os
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import pandas as pd

CSV_PATH = "history/price_history.csv"
COLUMNS = ["date", "ticker", "open", "high", "low", "close", "volume"]

def _load():
    if os.path.exists(CSV_PATH):
        return pd.read_csv(CSV_PATH)
    return pd.DataFrame(columns=COLUMNS)

def append_prices(rows):
    """
    여러 종목의 하루치 시세를 한 번에 누적 (읽기 1회 + 쓰기 1회).
    rows: [{"date": "...", "ticker": "...", "open":.., "high":.., "low":.., "close":.., "volume":..}, ...]
    같은 (date, ticker) 조합이 이미 있으면 새 값으로 덮어씀.
    """
    if not rows:
        return
    df = _load()
    new_df = pd.DataFrame(rows)
    df = pd.concat([df, new_df], ignore_index=True)
    df = df.drop_duplicates(subset=["date", "ticker"], keep="last")
    df = df.sort_values(["ticker", "date"]).reset_index(drop=True)
    df.to_csv(CSV_PATH, index=False)

def append_price(ticker, date, price):
    # 한 종목만 저장할 때 쓰는 얇은 래퍼 (내부적으로 append_prices 호출)
    append_prices([{
        "date": date,
        "ticker": ticker,
        "open": price["open"],
        "high": price["high"],
        "low": price["low"],
        "close": price["price"],
        "volume": price["volume"]
    }])

def get_high_low(ticker, days):
    df = _load()
    df = df[df["ticker"] == ticker]
    if df.empty:
        return None
    cutoff = (datetime.now(ZoneInfo("Asia/Seoul")) - timedelta(days=days)).strftime("%Y-%m-%d")
    df = df[df["date"] >= cutoff]
    if df.empty:
        return None
    return {
        "high": float(df["high"].max()),
        "low": float(df["low"].min())
    }

def get_high_low_3m(ticker):
    return get_high_low(ticker, days=90)

def get_high_low_1y(ticker):
    return get_high_low(ticker, days=365)
