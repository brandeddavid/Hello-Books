from flask_restful import Resource, Api
import json



class Allbooks(Resource):

    def __init__(self):

        self.books = [
            {
                'Title': 'The Lean Start Up',
                'Author': 'Eric Ries'
            },
            {
                'Title': 'Game of Thrones',
                'Author': 'Georgr R.R. Martin'
            }
        ]

    def get(self):

        return self.books

    def put(self, data):

        self.books.append(data)
        return json.dumps(self.books)


class Book(Resource):

    def put(self):

        pass

    def get(self):

        pass

