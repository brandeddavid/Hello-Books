from flask import Flask
from models import *

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():

    return 'Hello, World'


api.add_resource(Books.CreateBook, '/api/v1/books')
api.add_resource(Books.Book, '/api/v1/book/<string:book_id>')
api.add_resource(Users.Createuser, '/api/v1/auth/register')


if __name__ == '__main__':

    app.run(debug=True)
