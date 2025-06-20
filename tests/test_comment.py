import unittest

from business_logic import CommentBusinessLogic, AccountBusinessLogic, PostBusinessLogic
from repository import comment_access, account_access, post_access
from models import db
from main_app import app


class TestCommentBusinessLogic(unittest.TestCase):

    def setUp(self):
        print('running test CommentLogic')
        with app.app_context():
            db.create_all()
        self.logic = CommentBusinessLogic(comment_access)
        self.post_logic = PostBusinessLogic(post_access)
        self.account_logic = AccountBusinessLogic(account_access)

    def test_create_comment(self):
        with app.app_context():
            self.account_logic.create_account('comment_author', 'psw')
            author = self.account_logic.access.get_record_by(name='comment_author')
            self.post_logic.create_post(title='test_title', content='test_content', author=author, should_commit=True)
            post = self.post_logic.access.get_record_by(title='test_title')
            self.logic.create_comment(content='content', author_id=author.id, post_id=post.id)
            is_comment_count_more_than_zero = post.comments_count > 0
            self.assertTrue(is_comment_count_more_than_zero)

    # def test_like_comment(self):
    #     with app.app_context():
    #         self.account_logic.create_account('comment_author', 'psw')
    #         author = self.account_logic.access.get_record_by(name='comment_author')
    #         print(author)
    #         self.post_logic.create_post(title='test_title', content='test_content', author=author, should_commit=True)
    #         comment = self.logic.access.get_record_by(author_id=author.id)
    #         self.logic.like_comment(comment, author)
    #         likes = comment.likes_count
    #         is_more_than_zero = likes > 0
    #         self.assertTrue(is_more_than_zero)

    def tearDown(self):
        with app.app_context():
            db.drop_all()