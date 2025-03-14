from sqlalchemy.orm import Session
from database import SessionLocal
from models import TickerPrice
import pandas as pd

def write_data_to_sqlite(model, data: pd.DataFrame):
    """写入数据到 SQLite 数据库"""
    session = SessionLocal()
    try:
        records = data.to_dict(orient='records')
        session.bulk_insert_mappings(model, records)
        session.commit()
        print(f"数据已写入表 {model.__tablename__}")
    except Exception as e:
        print(f"写入数据失败: {e}")
    finally:
        session.close()

# 测试
data = pd.DataFrame({
    'Ticker': ['AAPL', 'MSFT'],
    'Date': [pd.Timestamp(2024, 1, 1).date(), pd.Timestamp(2024, 1, 1).date()],
    'Close': [150.0, 250.0],
    'Volume': [10000, 20000],
    'StockSplits': [0, 0],
    'Type': ['Stock', 'Stock']
})

write_data_to_sqlite(TickerPrice, data)
