from functions import log
from .db import db

def db_commit():
    try:
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        log(e, db_commit)
        return False