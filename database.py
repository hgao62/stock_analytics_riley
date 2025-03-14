from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# 连接 SQLite 数据库
DATABASE_URL = "sqlite:///stocks.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建数据库表
Base.metadata.create_all(bind=engine)
