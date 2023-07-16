import MeCab
tagger = MeCab.Tagger("-d /usr/lib/aarch64-linux-gnu/mecab/dic/mecab-ipadic-neologd") # TODO: 環境に合わせて変更する

def tokenizer(text):
    """
    Mecab で形態素解析を実施する
    """
    nodes = tagger.parseToNode(text)
    result = []
    while nodes:
        if nodes.surface != "":
            morpheme = {}
            s = nodes.feature.split(",")
            morpheme["surface"] = nodes.surface
            morpheme["base"] = s[6]
            morpheme["pos"] = s[0]
            morpheme["pos1"] = s[1]
            result.append(morpheme)
        nodes = nodes.next
    return result
