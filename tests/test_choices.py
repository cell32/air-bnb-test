import unittest
from flask import Flask, url_for
from flask_testing import TestCase
from src.app import app
from collections.abc import MutableMapping

# if os.environ.get("GITHUB_ACTIONS"):
#     from app import app
# else:
#     from src.app import app

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestChoicesPage(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_choices_page_rendering(self):
        response = self.client.get(url_for('show_choices', input_name='test_user'))
        self.assert200(response)

        # Check if the template is being used
        self.assert_template_used('choices.html')

        # Check if the expected content is present
        print(self.assert_context('input_name', 'test_user'))
        
# print("This is the path: ", sys.path)

if __name__ == '__main__':
    unittest.main()