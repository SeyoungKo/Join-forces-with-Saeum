from flask_restx import Resource, Api, Namespace
from flask import Flask, jsonify, request, json
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token
import config

status = ['VALID', 'INVALID']

cur = config.db()
cors = config.cors()

User = Namespace('User')
bcrypt = Bcrypt()
jwt = JWTManager()


@User.route('/register', methods=['POST'])
class Register(Resource):
    def post(self):
        """회원 정보 등록"""
        cursor = cur.cursor(buffered=True)
        id = request.get_json()['id']
        password = bcrypt.generate_password_hash(
            request.get_json()['password']).decode('utf-8')
        name = request.get_json()['name']
        tel = request.get_json()['tel']
        email = request.get_json()['email']

        reg_date = datetime.utcnow()

        sql = """INSERT INTO user(id, password, name, tel, email, reg_date, status)
                 VALUES ( %s, %s, %s, %s, %s, %s,%s)"""

        cursor.execute(sql, (str(id), str(password), str(name), str(tel), str(email), str(reg_date), str(status[0])))
        cur.commit()

        result = {
            'id': id,
            'password': password,
            'name': name,
            'tel': tel,
            'email': email
        }
        rtn = {'result': result}
        return json.dumps(rtn, default=str)


@User.route('/login', methods=['POST'])
class Login(Resource):
    def post(self):
        """사용자 로그인"""
        cursor = cur.cursor(buffered=True)
        id = request.get_json()['id']
        password = request.get_json()['password']
        access_date = datetime.utcnow()

        cursor.execute("SELECT * FROM user WHERE id = '" + str(id) + "'")
        row = cursor.fetchone()

        if bcrypt.check_password_hash(row[2], password):
            access_token = create_access_token(
                identity={
                    'user_key': row[0],
                    'id': row[1],
                    'name': row[4],
                    'tel': row[8],
                    'email': row[3]
                })
            result = access_token

            sql = """UPDATE user SET access_date = %s """
            cursor.execute(sql, (str(access_date),))
            cur.commit()
        else:
            message = {'error': "Invalid username, password"}
            result = json.dumps(message, default=str)

        return result
