import unittest

from business_logic import AccountBusinessLogic
from main_app import app
from models import db
from repository import account_access

class TestAccountLogic(unittest.TestCase):


    def setUp(self):
        print('running test AccountLogic')
        with app.app_context():
            db.create_all()
        self.account_logic = AccountBusinessLogic(account_access)

    def test_create_account(self):
        with app.app_context():
            self.account_logic.create_account(should_commit=True, name='testname', password='testpassword')
            new_account = self.account_logic.access.get_record_by_id(1)
            self.assertTrue(new_account)

    def tearDown(self):
        with app.app_context():
            db.drop_all()




if __name__ == '__main__':
    unittest.main()