"""
39. Zipfの法則
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
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
    rank = []
    rank_count = 1
    frequency = []

    for k, v in counter.most_common():
        rank.append(rank_count)
        frequency.append(v)
        rank_count += 1

    plt.plot(rank, frequency)

    plt.xlim(0, 500)
    plt.ylim(0, 10000)
    plt.title("単語の出現頻度")
    plt.xlabel("単語の出現頻度順位")
    plt.ylabel("出現頻度")
    plt.savefig("ch04/39.png")

run()
counter = Counter(word)
draw(counter)
