from flask import Flask, jsonify, request, json
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restx import Resource, Api
from user import User
from team import Team
from room import Room

app = Flask(__name__)
api = Api(app)
api.add_namespace(User, '/users')
api.add_namespace(Team, '/teams')
api.add_namespace(Room, '/rooms')
wsgi_app = app.wsgi_app

app.config['JWT_SECRET_KEY'] = 'secret'
app.config['MYSQL_DATABASE_CHARSET'] = 'utf-8'
app.config['CORS_HEADERS'] = 'Content-Type'

status = ['VALID', 'INVALID']

jwt = JWTManager(app)
CORS(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
