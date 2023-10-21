import os
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression

cdir = os.path.dirname(os.path.abspath(__file__))
X_train = pd.read_table(cdir + '/train.feature.txt')
Y_train = pd.read_table(cdir + '/train.txt')['CATEGORY']

# ロジスティック回帰モデルの学習
lr = LogisticRegression(max_iter=1000)
lr = lr.fit(X_train, Y_train)

# モデルの保存
with open(cdir + '/model.pickle', mode='wb') as f:
    pickle.dump(lr, f)
