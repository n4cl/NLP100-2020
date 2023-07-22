"""
40. 係り受け解析結果の読み込み（形態素）
形態素を表すクラスMorphを実装せよ．
このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．
さらに，係り受け解析の結果（ai.ja.txt.parsed）を読み込み，各文をMorphオブジェクトのリストとして表現し，冒頭の説明文の形態素列を表示せよ．
"""

import os
import CaboCha
from morph import Morph
from reader import read_ai

@read_ai
def create_parsed_file(line):
    cabocha = CaboCha.Parser()

    parse_result = cabocha.parse(line)
    lattice = parse_result.toString(CaboCha.FORMAT_LATTICE)
    return lattice

#create_parsed_file()
AI_PARSED_PATH = os.path.dirname(os.path.abspath(__file__)) + "/ai.ja.txt.parsed"
with open(AI_PARSED_PATH, "r", encoding="utf-8") as f:
    document = []
    morphemes = []
    for line in f:
        layer = line.split()
        if layer[:1] == "*" and len(layer) == 5:
            continue
        elif line == "EOS\n":
            if morphemes:
                document.append(morphemes)
            morphemes = []
            continue
        else:
            nodes = line.split("\t")
            if len(nodes) != 2:
                continue
            surface = nodes[0]
            node = nodes[1].split(",")
            morph = Morph(surface, node[5], node[0], node[1])
            morphemes.append(morph)
    for m in document[1]:
        print(m)
