import datetime

from sqlalchemy import (
    Column,
    DECIMAL,
    String,
    Integer,
    Date,
    create_engine, ForeignKey, Table
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine(
    "mysql+pymysql://root:?cwks19!16@127.0.0.1:3306/portal"
)
Base = declarative_base(bind=engine)