import unittest
import os
import sys
from src.app import app

# if os.environ.get("GITHUB_ACTIONS"):
#     from src.app import app
# else:
#     from src.app import app

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    # Testing the Login template with some fake data and see if it redirects
    def test_login_redirect(self):
        response = self.app.post("/echo_user_input", data={"user_input": "test_user", "user_password": "test_password"})
        self.assertEqual(response.status_code, 302)  # Expecting a redirect

    def test_login_redirected_url(self):
        response = self.app.post("/echo_user_input", data={"user_input": "test_user", "user_password": "test_password"})
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertIn(b"test_user", response.data)  # Assuming the username is included in the redirected URL

if __name__ == "__main__":
    unittest.main()