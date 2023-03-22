from datetime import datetime

from sqlalchemy import (
    Column,
    DECIMAL,
    String,
    Integer,
    Date,
    create_engine, ForeignKey, Table, DateTime
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine(
    "mysql+pymysql://root:?cwks19!16@127.0.0.1:3306/portal"
)
Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    fullname = Column(String(50))
    lastname = Column(String(50))
    nickname = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    registration_date = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"User({self.nickname})"

