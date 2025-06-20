import unittest
from main_app import app
from models import db
from business_logic import SignInBusinessLogic, SignUpBusinessLogic
from repository import AccountAccess

class TestSignInBusinessLogic(unittest.TestCase):
    def setUp(self):
        print('running test SignInLogic')
        with app.app_context():
            db.create_all()
        self.account_access = AccountAccess()
        self.logic = SignInBusinessLogic(self.account_access)
        self.sign_up_logic = SignUpBusinessLogic(self.account_access)

    def test_sign_in(self):
        with app.app_context():
            with app.test_request_context():
                self.sign_up_logic.sign_up('test_name', 'test_password')
                new_account = self.account_access.get_record_by_id(1)
                is_successfully_logged = self.logic.login(new_account, password='test_password')
        self.assertTrue(is_successfully_logged)

    def tearDown(self):
        with app.app_context():
            db.drop_all()