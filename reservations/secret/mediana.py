import random
from ippanel import Client


def env_setting(key, default=None):
    import os
    return os.environ.get(key, default)


api = Client(env_setting('API_KEY'))

sender = env_setting('SENDER')
summary = ""

code = random.randint(env_setting('MAX_CODE', 1000), env_setting('MIN_CODE', 9999))
