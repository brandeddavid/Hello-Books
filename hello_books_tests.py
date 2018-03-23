import unittest, app, json
from models import Users, Books


class Testcreateuser(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        self.user = Users('David', 'Mwangi','dmwangi', 'password123')

    def test_api_exists(self):

        res = self.app.get('/api/v1/auth/register')
        self.assertEqual(res.status_code, 200)


class Testcreatebooks(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        self.book = Books('The Lean Start up', 'Eric Ries', '354546422', 'Press Publisher', '10th November, 2010', 'N/A')

    def test_api_exists(self):

        res = self.app.get('/api/v1/books')
        self.assertEqual(res.status_code, 200)

    def test_create_books(self):

        res = self.app.post('/api/v1/books')
        self.assertEqual(res.status_code, 201)
        self.assertIn('The Lean Start up', str(res.data))

    def test_get_all_books(self):

        res = self.app.get('/api/v1/books')

        self.assertEqual(res.status_code, 201)



if __name__ == "__main__":
    unittest.main()
