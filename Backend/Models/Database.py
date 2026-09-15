from flask import g
import sqlite3

DATABASE = "road_damage.db"

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn
