# tests/test_integration.py

import unittest
import os
import sys
from flask_testing import TestCase
from src.app import app

# if os.environ.get("GITHUB_ACTIONS"):
#     from app import app
# else:
#     from src.app import app

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class IntegrationTest(TestCase):
    def create_app(self):
        return app

    # This test checks if accessing the root URL ("/") in the main page results in a successful and response status code 200.
    def test_main_page(self):
        response = self.client.get("/")
        self.assert200(response)
        self.assert_template_used("login.html")

    # This test simulates a POST request to "echo_user_input" with some fake data Login form
    def test_echo_input_redirect(self):
        response = self.client.post("/echo_user_input", data={"user_input": "test_user", "user_password": "test_password"})
        self.assertStatus(response, 302)  # Check if the response status is a redirect
        self.assertIn("/show_choices/test_user", response.headers["Location"])  # Check if the path is correct        

    # This test checks if accessing the "/show_choices/test_user" URL results in a successful 200 status code
    def test_show_choices_page(self):
        response = self.client.get("/show_choices/test_user")
        self.assert200(response)
        self.assert_template_used("choices.html") # check the template used and input previously passed in the Login fake data test
        self.assert_context("input_name", "test_user")

if __name__ == "__main__":
    unittest.main()