import pandas as pd
import yfinance as yf
from database import SessionLocal
from models import TickerPrice

def fetch_stock_data(ticker: str, period="1d"):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    
    if data.empty:
        print(f"获取 {ticker} 数据失败")
        return None

    data.reset_index(inplace=True)
    data["Ticker"] = ticker
    data["Type"] = "Stock"

    return data

def save_stock_data(ticker: str, period="1d"):
    data = fetch_stock_data(ticker, period)
    if data is not None:
        session = SessionLocal()
        records = data.to_dict(orient='records')
        session.bulk_insert_mappings(TickerPrice, records)
        session.commit()
        session.close()
        print(f"{ticker} 数据已存入数据库")

# 测试
save_stock_data("AAPL", "5d")

