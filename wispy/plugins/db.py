from peewee import *
import datetime

db = SqliteDatabase("wispy.db")
class BaseModel(Model):
    created = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = db

def register_callbacks(conn):
    conn.__dict__["conn"].db = db
