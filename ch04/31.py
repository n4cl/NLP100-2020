"""
31. 動詞
動詞の表層形をすべて抽出せよ．
"""

from reader import read_neko
from tokenizer import tokenizer

@read_neko
def run(line):
    tokens = tokenizer(line)
    for token in tokens:
        if token["pos"] == "動詞":
            print(token["surface"])

run()
