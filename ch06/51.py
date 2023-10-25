import os
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

cdir = os.path.dirname(os.path.abspath(__file__))
train = pd.read_table(cdir + '/train.txt')
valid = pd.read_table(cdir + '/valid.txt')
test = pd.read_table(cdir + '/test.txt')

# 前処理
def preprocessing(text):
    # 小文字化
    text = text.lower()
    # 記号の削除
    text = re.sub(r'[.,:;!?#%&"]', '', text)

    return text

train["TITLE"] = train["TITLE"].apply(preprocessing)

print(train.head())

# q: ngram_rangeは何？
# a: ngram_range=(1, 2)なら、1-gram, 2-gramの両方を計算する
count_vectorizer = CountVectorizer(min_df=5, ngram_range=(1, 2))

# トレーニングデータから特徴量を抽出
count_vectorizer.fit(train['TITLE'])
train_X = count_vectorizer.transform(train['TITLE'])
valid_X = count_vectorizer.transform(valid['TITLE'])
test_X = count_vectorizer.transform(test['TITLE'])

# 出力するためにデータフレームに変換する
train_X = pd.DataFrame(train_X.toarray(), columns=count_vectorizer.get_feature_names_out())
valid_X = pd.DataFrame(valid_X.toarray(), columns=count_vectorizer.get_feature_names_out())
test_X = pd.DataFrame(test_X.toarray(), columns=count_vectorizer.get_feature_names_out())

# データの出力
train_X.to_csv(cdir + '/train.feature.txt', sep='\t', index=False)
valid_X.to_csv(cdir + '/valid.feature.txt', sep='\t', index=False)
test_X.to_csv(cdir + '/test.feature.txt', sep='\t', index=False)
