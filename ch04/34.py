"""
34. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""

from reader import read_neko
from tokenizer import tokenizer

@read_neko
def run(line):
    tokens = tokenizer(line)
    temp = ""
    count = 0
    for token in tokens:
        if token["pos"] == "名詞":
            temp += token["surface"]
            count += 1
            continue

        if temp != "" and count > 1:
            print(temp)
        temp = ""
        count = 0
        continue

run()
