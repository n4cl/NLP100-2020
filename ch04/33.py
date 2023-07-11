"""
33. 「AのB」Permalink
2つの名詞が「の」で連結されている名詞句を抽出せよ．
"""

from reader import read_neko
from tokenizer import tokenizer

@read_neko
def run(line):
    tokens = tokenizer(line)
    a = ""
    noun_phrase = False
    for token in tokens:
        if a == "" and token["pos"] == "名詞":
            a = token["surface"]
            continue

        if token["pos"] == "助詞" and token["surface"] == "の":
            noun_phrase = True
            continue

        if noun_phrase and token["pos"] == "名詞":
            print(a + "の" + token["surface"])

        noun_phrase = False
        a = ""

run()

