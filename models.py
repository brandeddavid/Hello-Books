from flask_restful import Resource, Api


class Users(object):

    def __init__(self, fname, sname, username, password):
        self.firstname = fname
        self.sname = sname
        self.username = username
        self.password = password

        self.users = []

    class Createuser(Resource):

        def get(self):

            pass

        def put(self):

            pass


class Books(object):

    def __init__(self, title, author, isbn, publisher, publish_date, edition):

        self.title = title
        self.author = author
        self.isbn = isbn
        self.publisher = publisher
        self.publish_date = publish_date
        self.edition = edition

        self.books = []

    class CreateBook(Resource):

        def put(self):

            pass

        def get(self):

            pass

    class Book(Resource):

        def get(self):

            pass

