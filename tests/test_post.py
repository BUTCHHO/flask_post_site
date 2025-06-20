import unittest

from main_app import app
from business_logic import PostBusinessLogic
from repository import post_access
from models import Account, Post, db


class TestPostBusinessLogic(unittest.TestCase):


    def setUp(self):
        print('running test PostLogic')
        with app.app_context():
            db.create_all()
        self.post_logic = PostBusinessLogic(post_access)

    def test_create_post(self):
        with app.app_context():
            author = Account(name='test_name', password='test_psw')
            title = 'test_title'
            content = 'test_content'
            posts_before = post_access.get_all_records()
            len_before = len(posts_before)
            self.post_logic.create_post(title=title, content=content, author=author, should_commit=False)
            posts_after = post_access.get_all_records()
            len_after = len(posts_after)
            result = len_after > len_before
            self.assertTrue(result)

    def test_like_post(self):
        with app.app_context():
            liker = Account(name='test_liker', password='test_psw')
            likeable_post = Post(title='test_title', content='test_content', author_id=1, creation_date='date')
            likes_before = likeable_post.likes_count
            self.post_logic.like_post(likeable_post, liker, should_commit=False)
            likes_after = likeable_post.likes_count
            is_success = likes_after > likes_before
            self.assertTrue(is_success)

    def tearDown(self):
        with app.app_context():
            db.drop_all()

# class TestAlotOfPosts(unittest.TestCase):
#
#     def setUp(self):
#         self.posts_count = 1000
#         with app.app_context():
#             db.create_all()
#         self.logic = PostBusinessLogic(post_access)
#
#     def test_create_lots_of_posts(self):
#         with app.app_context():
#             author = Account(name='test_name', password='test_psw')
#             for i in range(self.posts_count):
#                 print(f'on {i} iteration')
#                 title = f'title{i}'
#                 content = 'content'
#                 self.logic.create_post(title,content,author)
#
#     # def tearDown(self):
#     #     with app.app_context():
#     #         db.drop_all()
#
# if __name__ == '__main__':
#     unittest.main()