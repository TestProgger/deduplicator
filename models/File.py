from peewee import BigIntegerField, TextField, BigIntegerField, TimestampField, CharField, DateTimeField
from models.BaseModel import BaseModel


from utils.time import get_timestamp_now


class File(BaseModel):
    name = TextField()
    size = BigIntegerField()

    atime = TimestampField()
    mtime = TimestampField()
    ctime = TimestampField()

    absolute_path = TextField()

    hashsum = CharField(max_length=32)

    created_at = DateTimeField(default=get_timestamp_now)
