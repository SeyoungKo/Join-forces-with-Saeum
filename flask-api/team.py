from flask_restx import Resource, Api, Namespace
from flask import Flask, jsonify, request, json
import config
import hashlib

status = ['VALID', 'INVALID']
cur = config.db()
cors = config.cors()

Team = Namespace('Team')


class Hash:
    def hashurl(self, team_key, teamname):
        url = str(team_key) + str('/') + str(teamname)
        hash = hashlib.sha1()
        hash.update(str(url).encode('utf-8'))
        rtn_url = hash.hexdigest()[:10]


        cursor = cur.cursor(buffered=True)
        cursor.execute("UPDATE team SET invite_url = '" + str(rtn_url) + "'" + " WHERE team_key = " + "'" + str(team_key)+"'")
        cur.commit()
        return str(rtn_url)


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

            url = Hash.hashurl(self, row2[0], name)

            json_res = {
                'response' : "ok"
            }
            rtn = {'result': json_res}
            json_res = json.dumps(rtn, default=str)

            # 역슬래시 제거
            clear = json_res.replace("\\", "")
            result = json.loads(clear)

        else:
            message = {'duplicate': "Dupicate teamname"}
            result = json.dumps(message, default=str)

        return result


@Team.route('/<user_key>', methods=['GET'])
class Load(Resource):
    def get(self, user_key):
        """팀 목록 조회"""
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


@Team.route('/<invite_url>/<user_key>', methods=['GET'])
class Verify(Resource):
    def get(self, invite_url, user_key):
        """url으로 팀 조회"""
        param1 = invite_url
        param2 = user_key

        cursor = cur.cursor(buffered=True)
        cursor.execute("SELECT * FROM team WHERE invite_url = '" + str(param1) + "'")
        row = cursor.fetchone()

        team_key = row[0]
        name = row[1]
        status = row[2]
        invite_url = row[3]
        created_by = row[4]

        rst = {
            'team_key' : team_key,
            'name' : name,
            'status' : status,
            'invite_url' : invite_url,
            'created_by' : created_by
        }

        if type(row) is not None:
            sql = """insert into affiliation(user_key, team_key)
                       values (%s, %s)"""
            cursor.execute(sql, (str(param2), str(team_key)))

            cur.commit()

            json_data = json.dumps(rst, default=str)
            # 역슬래시 제거
            clear = json_data.replace("\\", "")
            result = json.loads(clear)

        else:
            message = {'not found': "Team does not exist"}
            result = json.dumps(message, default=str)

        return result

