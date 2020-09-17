import mysql.connector as mysql
from flask_cors import CORS


def db():
    cur = mysql.connect(user='seyoung', password='seyoung', host='localhost', database='graduation')
    return cur


def cors():
    return CORS()