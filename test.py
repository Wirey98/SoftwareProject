# 29.03.2021 https://www.youtube.com/watch?v=1aHNs1aEATg
from app import app
import unittest

class FlaskTestCase(unittest.TestCase):



    # To esnure pages are loading
    def test_index(self):
        tester=app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # To esnure login page is loading
    def test_login_page(self):
        tester=app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Create an Account' in response.data)

    # Testing the login with correct credentials
    def test_login_correct(self):
        tester=app.test_client(self)
        response = tester.post(
            '/',
            data=dict(name="test", password="test"),
            follow_redirect=True
        )
        self.assertIn(b'Logged In', response.data)

    # Testing the login with incorrect credentials

    # Testing logout

if __name__ == '__main__':
    unittest.main()


    