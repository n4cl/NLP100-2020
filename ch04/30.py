# 30. 形態素解析結果の読み込み
from tokenizer import tokenizer

if __name__ == '__main__':
    res = tokenizer("形態素解析結果の読み込み")
    for m in res:
        print(m["surface"], m["base"], m["pos"], m["pos1"])
