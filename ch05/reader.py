import os

AI_PATH = os.path.dirname(os.path.abspath(__file__)) + "/ai.ja.txt"
AI_PATH_PARSED = os.path.dirname(os.path.abspath(__file__)) + "/ai.ja.txt.parsed"

def read_ai(func):
    def wrapper(*args, **kwargs):
        with open(AI_PATH, "r", encoding="utf-8") as f, open(AI_PATH_PARSED, "w", encoding="utf-8") as p:
            for line in f:
                res = func(line, *args, **kwargs)
                p.write(f"{res}\n")
    return wrapper
