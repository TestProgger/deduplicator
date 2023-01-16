from models.db import db
from models.BaseModel import BaseModel
from models.File import File


def create_tables():
    db.create_tables([File, ])
