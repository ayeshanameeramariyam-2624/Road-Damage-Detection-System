import sqlite3

DATABASE = "road_damage.db"

def get_connection():
    return sqlite3.connect(DATABASE)
