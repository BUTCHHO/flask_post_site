from werkzeug.security import generate_password_hash
from functions import write_logs
from login_manage import UserMixin
from models import db_commit
from models.account import Account, db
from .ParentAccess import ModelAccess


class AccountAccess(ModelAccess, UserMixin):

    def __init__(self):
        super().__init__(model=Account)

account_access = AccountAccess()