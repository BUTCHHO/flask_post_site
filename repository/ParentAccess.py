from typing import Type

from functions import write_logs
from models import db, db_commit


class ModelAccess:

    def __init__(self, model):
        self.model = model
        self.db = db
    @write_logs
    def delete_all_records(self):
        self.model.query.delete()
        db_commit()

    @write_logs
    def delete_record_by_id(self, object_id):
        self.model.query.filter_by(id=object_id).delete()
        db_commit()

    @write_logs
    def get_all_records(self):
        return self.model.query.all()

    @write_logs
    def get_record_by_id(self, object_id):
        return self.model.query.filter_by(id=object_id).first()

    @write_logs
    def get_record_by(self, **kwargs):
        return self.model.query.filter_by(**kwargs).first()


    @write_logs
    def write_to_db(self, **kwargs):
        try:
            record = self.model(**kwargs)
            db.session.add(record)
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False




