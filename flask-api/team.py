from flask_restx import Resource, Api, Namespace
from flask import Flask, jsonify, request, json
import config

status = ['VALID', 'INVALID']
cur = config.db()
cors = config.cors()

Team = Namespace('Team')

@Team.route('/enroll', methods=['POST'])
class Enroll(Resource):
    def post(self):
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

@Team.route('/<user_key>', methods=['GET'])
class Load(Resource):
    def get(self, user_key):
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
                    'team_key' : row[0],
                    'name': row[1],
                    'status': row[2],
                    'invite_url': row[3],
                    'created_by': row[4]
                }
                multiple.append(rst)

        json_data = json.dumps(multiple, default=str)
        # 역슬래시 제거
        clear = json_data.replace("\\","")
        result = json.loads(clear)

        return result
