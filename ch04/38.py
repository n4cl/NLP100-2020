"""
38. ヒストグラム
単語の出現頻度のヒストグラムを描け．
ただし，横軸は出現頻度を表し，1から単語の出現頻度の最大値までの線形目盛とする．
縦軸はx軸で示される出現頻度となった単語の異なり数（種類数）である．
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
    f = {}
    max_x_value = max(counter.values())
    for k, v in counter.items():
        if v in f:
            f[v] += 1
        else:
            f[v] = 1
    x = [v for v in f.values()]
    plt.hist(x=x, bins=100)
    plt.xlim(0, max_x_value)
    plt.title("単語の出現頻度")
    plt.xlabel("出現頻度")
    plt.ylabel("単語の異なり数")
    plt.savefig("ch04/38.png")

run()
counter = Counter(word)
draw(counter)
