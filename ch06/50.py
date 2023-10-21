import os
import pandas as pd
from sklearn.model_selection import train_test_split

cdir = os.path.dirname(os.path.abspath(__file__))
news = pd.read_table(cdir + '/newsCorpora.csv', header=None)
news.columns = ['ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP']

# Reuters”, “Huffington Post”, “Businessweek”, “Contactmusic.com”, “Daily Mail”の5社のみを対象とする
specific_news = news[news['PUBLISHER'].isin(
    ['Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail'])]

# TITLEとCATEGORYの列のみを抽出する
specific_news = specific_news[['TITLE', 'CATEGORY']]

# データをシャッフルする
# q: このrandom_stateは何？
# a: 乱数のシード値。同じ値を指定すると、同じ乱数が生成される。
# q: このfracは何？
# a: 0.5なら、半分のデータを返す。1なら、全てのデータを返す。
specific_news = specific_news.sample(frac=1, random_state=0)


# データを学習用と評価用に分割する
# stratify: ラベルの比率を維持する
train_data, valid_data = train_test_split(specific_news, test_size=0.2, random_state=0, stratify=specific_news['CATEGORY'])

# 評価用データを評価用とテスト用に分割する
valid_data, test_data = train_test_split(valid_data, test_size=0.5, random_state=0, stratify=valid_data['CATEGORY'])

# データの保存
train_data.to_csv(cdir + '/train.txt', sep='\t', index=False)
valid_data.to_csv(cdir + '/valid.txt', sep='\t', index=False)
test_data.to_csv(cdir + '/test.txt', sep='\t', index=False)

