import unittest

from main_app import app
from business_logic import UserBusinessLogic
from repository import account_access
from models import Account, db

class TestUserLogic(unittest.TestCase):


    def setUp(self):
        print('running test UserLogic')
        with app.app_context():
            db.create_all()
        self.user_logic = UserBusinessLogic('this guy dont really needs access')

    def test_follow_to_user(self):
        with app.app_context():
            self.first_user = Account(id=1, name='test_name', password='test_psw')
            self.second_user = Account(id=2, name='test_name2', password='test_psw2')
            self.user_logic.follow_to_user(self.first_user, self.second_user)
            did_followers_count_increased = self.second_user.followers_count > 0
            self.assertTrue(did_followers_count_increased)

    def test_unfollow_from_user(self):
        with app.app_context():
            self.first_user = Account(id=1, name='test_name', password='test_psw')
            self.second_user = Account(id=2,name='test_name2', password='test_psw2')
            self.user_logic.follow_to_user(self.first_user, self.second_user)
            self.user_logic.unfollow_from_user(self.first_user, self.second_user)
            is_followers_count_zero = self.second_user.followers_count == 0
            self.assertTrue(is_followers_count_zero)

    def tearDown(self):
        with app.app_context():
            db.drop_all()