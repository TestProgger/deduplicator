from peewee import SqliteDatabase

db = SqliteDatabase('db.sqlite3')
db.connect()
