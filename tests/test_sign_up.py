import unittest
from business_logic import SignUpBusinessLogic
from repository import AccountAccess
from main_app import app
from models import db


class TestSignUpBusinessLogic(unittest.TestCase):

    def setUp(self):
        print('running test SignUpLogic')
        with app.app_context():
            db.drop_all()
            db.create_all()
        self.account_access = AccountAccess()
        self.logic = SignUpBusinessLogic(self.account_access)

    def test_sign_up(self):
        with app.app_context():
            name = 'test_name'
            password = 'test_password'
            self.logic.sign_up(name, password)
            new_account = self.account_access.get_record_by_id(1)
            self.assertTrue(new_account)

    def tearDown(self):
        with app.app_context():
            db.drop_all()
