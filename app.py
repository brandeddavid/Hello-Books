from flask import Flask
from models import *

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():

    return 'Hello, World'


api.add_resource(Allbooks, '/api/v1/books')
api.add_resource(Book, '/api/v1/book/<string:book_id>')


if __name__ == '__main__':

    app.run(debug=True)
