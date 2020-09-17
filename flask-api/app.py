from flask import Flask, jsonify, request, json
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restx import Resource, Api
from flask_socketio import SocketIO, emit
from flask import session
from user import User
from team import Team
from room import Room

app = Flask(__name__)
api = Api(app, version='1.0',
               title="dure api server",
               description="graduation project api server",
          )

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

socketio = SocketIO(app, ping_timeout=30, cors_allowed_origins="*")


@socketio.on('SEND_MESSAGE', namespace="/chat")
def connect(data):
    message = data['message']
    user_key = data['user_key']
    team_key = data['team_key']

    print("connected!")
    print(message)

    emit('MESSAGE',{'message' : message})


@socketio.on('disconnect', namespace="/chat")
def disconnect():
    session.clear()
    print("disconnected")

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
    socketio.run(app, debug=True, host='127.0.0.1', port=8000)
