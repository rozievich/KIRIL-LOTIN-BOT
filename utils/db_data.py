from datetime import datetime
from sqlalchemy import Column, Integer, String, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql+psycopg2://postgres:black0613@localhost:5432/kirlat_db")
Base = declarative_base()
Session = sessionmaker(bind=engine)

session = Session()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, nullable=True, unique=True)
    created_at = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return self.user_id


class Channel(Base):
    __tablename__ = "channels"
    id = Column(Integer, primary_key=True, index=True)
    channel_url = Column(String(128), unique=True, nullable=True)
    channel_id = Column(String(128), unique=True, nullable=True)
    created_at = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return self.channel_id
