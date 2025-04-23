# Author: Rikki Villafranca
# Date: 4/19/2025
# Description: Uses SQLAchemy to store metadata regarding each fanfic which will allow search/filter, track updates, display fields, and avoid redownloading fanfics in my archive.


# Declarations
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()

#######################################
# Function: Fanfic(Base)
# Description: Class function to create
# the fields for the database.
#######################################
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


#######################################
# Function: get_engine()
# Description: Function to create the 
# database named fanfic_archive.db.
#######################################
def get_engine(db_url="sqlite:///database/fanfic_archive.db"):
    return create_engine(db_url)


#######################################
# Function: init_db()
# Description: Function to init the 
# database, which calls get_engine()
# function. It uses Base module to
# create the metadata with all the 
# fields of the database.
#######################################
def init_db():
    engine= get_engine()
    Base.metadata.create_all(engine)
