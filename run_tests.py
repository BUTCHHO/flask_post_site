import unittest
from main_app import app
from models import db


def run_tests():
    loader = unittest.TestLoader()
    suite = loader.discover('tests')
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    return result.wasSuccessful()

if __name__ == '__main__':
    if run_tests():
        print('Tests passed!')
    else:
        print('Tests failed')
    with app.app_context():
        db.drop_all()