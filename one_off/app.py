from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

class Books(Resource):
    def get(self):
        return {
            'Michael Crichton' : 'Jurassic Park',
            'Frank Herbert' : 'Dune',
            'Mario Puzo' : 'The Godfather'
        }

    def post(self):
        parser.add_argument('book', type=str)
        args = parser.parse_args()

        return {
            'status' : True,
            'book' : '{} added successfully.'.format(args['book'])
        }
    
    def put(self, id):
        parser.add_argument('book', type=str)
        #args = parser.parse_args()

        return {
            'id': id,
            'status': True,
            'book': 'The book with id {} was updated'.format(id)
        }
        
api.add_resource(Books, '/', '/update/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)