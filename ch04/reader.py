import os

NEKO_PATH = os.path.dirname(os.path.abspath(__file__)) + "/neko.txt"


def read_neko(func):
    def wrapper(*args, **kwargs):
        with open(NEKO_PATH, "r", encoding="utf-8") as f:
            for line in f:
                func(line, *args, **kwargs)
    return wrapper
