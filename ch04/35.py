"""
35. 単語の出現頻度Permalink
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""

from collections import Counter

from reader import read_neko
from tokenizer import tokenizer

word = []

@read_neko
def run(line):
    tokens = tokenizer(line)
    for token in tokens:
        word.append(token["surface"])
run()
counter = Counter(word)
print(counter.most_common())
