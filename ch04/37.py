"""
37. 「猫」と共起頻度の高い上位10語
「猫」とよく共起する（共起頻度が高い）10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
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
    temp = []
    is_cat = False
    for token in tokens:
        surface = token["surface"]
        if surface == "猫":
            is_cat = True
        temp.append(surface)

    if is_cat:
        word.extend(temp)

def draw(counter):
    del counter["猫"]
    w, v = zip(*counter.most_common(10))
    plt.bar(x=w, height=v)
    plt.ylim(0, 500)
    plt.title("「猫」と共起頻度の高い上位10語")
    plt.xlabel("単語")
    plt.ylabel("出現頻度")
    plt.savefig("ch04/37.png")

run()
counter = Counter(word)
draw(counter)
