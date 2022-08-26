from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Class(Resource):
    def get(self):
        response = jsonify({
            'id': 1,
            'username': "admin",
            'email': "admin@example.com",
            'password': "Admin123"
        })
        return response

api.add_resource(Class, '/login')

if __name__ == "__main__":
    app.run(debug=True)
