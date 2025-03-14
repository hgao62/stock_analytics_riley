from sqlalchemy.orm import Session
from database import SessionLocal
from models import TickerPrice
import pandas as pd

def read_stock_data(ticker):
    """查询特定股票数据"""
    session = SessionLocal()
    try:
        results = session.query(TickerPrice).filter(TickerPrice.Ticker == ticker).all()
        data = [{"Ticker": r.Ticker, "Date": r.Date, "Close": r.Close, "Volume": r.Volume} for r in results]
        df = pd.DataFrame(data)
        return df
    finally:
        session.close()

# 测试
df = read_stock_data("AAPL")
print(df)
