from flask import Flask, jsonify, request, json
import mysql.connector as mysql
from datetime import datetime
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'secret'
app.config['MYSQL_DATABASE_CHARSET'] = 'utf-8'

status = ['VALID', 'INVALID']

jwt = JWTManager(app)
CORS(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

cur = mysql.connect(user='seyoung', password='seyoung', host='localhost', database='graduation')

@app.route('/users/register', methods=['POST'])
def register():
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

    cursor.execute(sql,(str(id), str(password), str(name), str(tel), str(email), str(reg_date), str(status[0])))
    cur.commit()

    result = {
        'id': id,
        'password': password,
        'name': name,
        'tel': tel,
        'email': email
    }
    rtn = {'result':result}
    return json.dumps(rtn, default=str)


@app.route('/users/login', methods=['POST'])
def login():
    cursor = cur.cursor(buffered=True)
    id = request.get_json()['id']
    password = request.get_json()['password']
    access_date = datetime.utcnow()

    cursor.execute("SELECT * FROM user WHERE id = '" + str(id) + "'")
    row = cursor.fetchone()

    if bcrypt.check_password_hash(row[2], password):
        access_token = create_access_token(
            identity={
                'user_key' : row[0],
                'id' : row[1],
                'name' : row[4],
                'tel' : row[8],
                'email': row[3]
            })
        result = access_token

        sql = """UPDATE user SET access_date = %s """
        cursor.execute(sql, (str(access_date),))
        cur.commit()
    else:
        message = {'error' : "Invalid username, password"}
        result = json.dumps(message, default=str)

    return result

@app.route('/teams/enroll', methods=['POST'])
def enroll():
    cursor = cur.cursor(buffered=True)
    name = request.get_json()['teamname']
    id = request.get_json()['id']

    cursor.execute("SELECT * FROM user WHERE id = '" + str(id) + "'")
    row = cursor.fetchone()
    rowcount = cursor.rowcount

    created_by = row[4]

    cursor.execute("SELECT * FROM team WHERE name ='" + str(name) + "'")
    count = cursor.rowcount

    if count == 0 and rowcount != 0:
        sql = """insert into team(name, status, created_by)
                values (%s, %s, %s)"""
        cursor.execute(sql, (str(name), str(status[0]), str(created_by)))
        cur.commit()

        cursor.execute("SELECT team_key FROM team WHERE name = '" + str(name) +"'" + " AND created_by = " + "'" + str(created_by)+"'")
        row2 = cursor.fetchone()

        sql = """insert into affiliation(user_key, team_key)
                   values (%s, %s)"""
        cursor.execute(sql, (str(row[0]), str(row2[0])))
        cur.commit()

        result = {
            'name': name,
            'created_by': created_by
        }
        rtn = {'result': result}
        result = json.dumps(rtn, default=str)

    else:
        message = {'duplicate': "Dupicate teamname"}
        result = json.dumps(message, default=str)

    return result

@app.route('/teams/<user_key>', methods=['GET'])
def load(user_key):
    param = user_key

    cursor = cur.cursor(buffered=True)
    cursor.execute("SELECT * FROM affiliation WHERE user_key = '" + str(param) + "'")
    row = cursor.fetchall()

    team_keys = []
    for i in range(len(row)):
        team_keys.append(row[i][1])

    multiple =[]

    for i in range(len(team_keys)):
        cursor = cur.cursor(buffered=True)
        cursor.execute("SELECT * FROM team WHERE team_key = '" + str(team_keys[i]) + "'")
        row = cursor.fetchone()

        if type(row) is not None:
            rst = {
                'name': row[1],
                'status': row[2],
                'invite_url': row[3],
                'created_by': row[4]
            }
            multiple.append(rst)

    result = json.dumps(multiple, default=str)
    return result

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)