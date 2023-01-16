from peewee import Model
from peewee import AutoField
from models.db import db


class BaseModel(Model):
    id = AutoField(primary_key=True)

    class Meta:
        database = db
