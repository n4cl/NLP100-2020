"""
36. 頻度上位10語Permalink
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
"""

from collections import Counter

from reader import read_neko
from tokenizer import tokenizer
import japanize_matplotlib
from matplotlib import pyplot as plt

word = []

@read_neko
def run(line):
    tokens = tokenizer(line)
    for token in tokens:
        word.append(token["surface"])

def draw(counter):
    w, v = zip(*counter.most_common(10))
    plt.bar(x=w, height=v)
    plt.ylim(0, 10000)
    plt.title("頻度上位10語")
    plt.xlabel("単語")
    plt.ylabel("出現頻度")
    plt.savefig("ch04/36.png")

run()
counter = Counter(word)
draw(counter)
