"""
41. 係り受け解析結果の読み込み（文節・係り受け）
40に加えて，文節を表すクラスChunkを実装せよ．
このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
さらに，入力テキストの係り受け解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，冒頭の説明文の文節の文字列と係り先を表示せよ．
本章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

import os
from morph import Morph
from chunk import Chunk


AI_PARSED_PATH = os.path.dirname(os.path.abspath(__file__)) + "/ai.ja.txt.parsed"
with open(AI_PARSED_PATH, "r", encoding="utf-8") as f:
    document = []
    sentence = []
    chunk = Chunk()
    ds_list = []
    for line in f:
        layer = line.split()
        if len(layer) == 5 and layer[0] == "*":

            # 係り先の読み込み
            if layer[2] == "-1D":
                ds_list.append((int(layer[1]), -1))
            else:
                ds_list.append((int(layer[1]), int(layer[2][:-1])))

            # 文節の読み込み
            if chunk.morphs:
                sentence.append(chunk)
            chunk = Chunk()

            continue
        elif line == "EOS\n":
            # 文末の処理
            if chunk.morphs:
                sentence.append(chunk)

                for src, dst in ds_list:
                    if dst != -1:
                        sentence[src].set_dst(dst)
                        sentence[dst].add_src(src)
                ds_list = []

                document.append(sentence)
            sentence = []
            # 連続するEOSを考慮して chunkを初期化
            chunk = Chunk()
            continue
        else:
            # 形態素の読み込み
            nodes = line.split("\t")
            # 空白と改行を除外
            if len(nodes) != 2:
                continue
            surface = nodes[0]
            node = nodes[1].split(",")
            morph = Morph(surface, node[5], node[0], node[1])
            chunk.add_morph(morph)
    for c in document[1]:
        print(c)
