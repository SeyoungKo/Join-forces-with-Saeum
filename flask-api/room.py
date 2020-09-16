from flask_restx import Resource, Api, Namespace
from flask import Flask, jsonify, request, json
from datetime import datetime
import config

status = ['VALID', 'INVALID']
cur = config.db()
cors = config.cors()

Room = Namespace('Room')

@Room.route('/enroll', methods=['POST'])
class Enroll(Resource):
    def post(self):
        cursor = cur.cursor(buffered=True)
        team_key = request.get_json()['team_key']
        roomname = request.get_json()['roomname']
        user_key = request.get_json()['user_key']
        created_at = datetime.utcnow()

        sql = """insert into room(created_at, user_key, roomname, last_date, team_key)
                          values (%s, %s, %s, %s, %s)"""
        cursor.execute(sql, (str(created_at), str(user_key), str(roomname), str(created_at), str(team_key)))
        cur.commit()

        result = {
            'roomname': roomname
        }
        rtn = {'result' : result}
        return json.dumps(rtn, default=str)

@Room.route('/<user_key>/<team_key>', methods=['GET'])
class Load(Resource):
    def get(self, user_key, team_key):
        param1 = user_key
        param2 = team_key

        cursor = cur.cursor(buffered=True)
        cursor.execute("SELECT roomname FROM room WHERE user_key = '" + str(param1) + "'" + " AND team_key = " + "'" + str(
            param2) + "'")

        row = cursor.fetchall()

        multiple =[]
        for i in range(len(row)):
            rst = {
                'roomname' : row[i][0]
            }
            multiple.append(rst)

        json_data = json.dumps(multiple, default=str)
        # 역슬래시 제거
        clear = json_data.replace("\\","")
        result = json.loads(clear)

        return result