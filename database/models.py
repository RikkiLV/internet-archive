# Author: Rikki Villafranca
# Date: 4/19/2025
# Description: Uses SQLAchemy to store metadata regarding each fanfic which will allow search/filter, track updates, display fields, and avoid redownloading fanfics in my archive.


# Declarations
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()

class Fanfic(Base):
    __tablename__ = 'fanfics'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    source = Column(String)
    story_id = Column(String)
    filepath = Column(String)
    summary = Column(Text)
    last_checked = Column(DateTime, default=datetime.utcnow)


def get_engine(db_url="sqlite:///database/fanfic_archive.db"):
    return create_engine(db_url)


def init_db():
    engine= get_engine()
    Base.metadata.create_all(engine)
