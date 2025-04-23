# Author: Rikki Villafranca
# Date: 4/19/2025
# Description: CRUB functions to handle create, read, update, and delete for fanfics in the database created by models.py.


# Declarations
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from database.models import Fanfic, get_engine
from datetime import datetime

engine = get_engine()
Session = sessionmaker(bind=engine)


#######################################
# Function: add_fanfic()
# Description: Passes the all db fields
# as parameters. Creates a session for 
# adding all fields in the database.
# Validates whether fanfic exists.
#######################################
def add_fanfic(title, author, source, story_id, filepath, summary=""):
    session = Session()
    try:
        fanfic = Fanfic(
            title=title,
            author=author,
            source=source,
            story_id=story_id,
            filepath=filepath,
            summary=summary
        )
        session.add(fanfic)
        session.commit()
        return fanfic
    except IntegrityError:
        session.rollback()
        print("Fanfic already exists.")
    finally:
        session.close()


#######################################
# Function: get_fanfic_by_site_id()
# Description: A function that query to 
# grab a fanfic from the database by 
# story_id.
#######################################
def get_fanfic_by_site_id(source, story_id):
    session = Session()
    fanfic = session.query(Fanfic).filter_by(source=source, story_id=story_id).first()
    session.close()
    return fanfic


#######################################
# Function: list_fanfics()
# Description: Function to query the list
# all the fanfic in the database.
#######################################
def list_fanfics(source=None):
    session = Session()
    query = session.query(Fanfic)
    if source:
        query = query.filter_by(source=source)
    results = query.all()
    session.close()
    return results


#######################################
# Function: update_last_checked()
# Description: Function that filters
# the db by story_id and checks on the 
# datetime of the fanfic.
#######################################
def update_last_checked(source, story_id):
    session = Session()
    fanfic = session.query(Fanfic).filter_by(source=source, story_id=story_id).first()
    if fanfic:
        fanfic.last_checked = datetime.utcnow()
        session.commit()
    session.close()


#######################################
# Function: delete_fanfic()
# Description: Function that filters
# the db by story_id and deletes the 
# fanfic from the db.
#######################################
def delete_fanfic(source, story_id):
    session = Session()
    fanfic = session.query(Fanfic).filter_by(source=source, story_id=story_id).first()
    if fanfic:
        session.delete(fanfic)
        session.commit()
    session.close()


#######################################
# Function: get_engine()
# Description: Function that passes a
# a searched term, which is filters
# all fields to find the fanfic with
# associated terms in the db. 
#######################################
def search_fanfics(term):
    session = Session()
    results = session.query(Fanfic).filter(
        (Fanfic.title.ilike(f"%{term}%")) | (Fanfic.author.ilike(f"%{term}%"))
    ).all()
    session.close()
    return results

