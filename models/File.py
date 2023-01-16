from peewee import BigIntegerField, TextField, BigIntegerField, TimestampField, CharField, DateTimeField
from BaseModel import BaseModel

from utils import get_timestamp_now


class File(BaseModel):
    name = TextField()
    size = BigIntegerField()

    atime = TimestampField()
    mtime = TimestampField()
    ctime = TimestampField()

    hashsum = CharField(max_length=32)

    created_at = DateTimeField(default=get_timestamp_now)
