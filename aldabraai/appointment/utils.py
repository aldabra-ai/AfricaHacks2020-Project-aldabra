import random
import string
import uuid

DEFAULT_CHAR_STRING = string.ascii_lowercase + string.digits

def generate_random_string(chars=DEFAULT_CHAR_STRING, size=10):
    return ''.join(random.choice(chars) for _ in range(size))


def generate_uuid(use_host:bool, use_id:bool, use_time:bool, rand:False):
    if (use_host, use_id, use_time):
        return uuid.uuid1()