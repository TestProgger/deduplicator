from datetime import datetime


def get_timestamp_now():
    return int(datetime.now().timestamp())
