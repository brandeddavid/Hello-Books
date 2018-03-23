import unittest, app, json

# book = app.Allbooks()
#
# print(book.get())


class Testcreatebooks(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        self.book = {'Title': 'The Lean Start up'}

    def test_create_books(self):

        res = self.app.post('/api/v1/books', data=self.book)
        self.assertEqual(res.status_code, 201)
        self.assertIn('The Lean Start up', str(res.data))


class Testgetallbooks(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def test_get_all_books(self):

        res = self.app.get('/api/v1/books')

        self.assertEqual(res.status_code, 201)



if __name__ == "__main__":
    unittest.main()
