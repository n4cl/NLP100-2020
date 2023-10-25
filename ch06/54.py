import os
import pickle
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score

cdir = os.path.dirname(os.path.abspath(__file__))

def load_model():
    with open(cdir + '/model.pickle', mode='rb') as f:
        model = pickle.load(f)
    return model

lr = load_model()

# データの読み込み
X_train = pd.read_table(cdir + '/train.feature.txt')
Y_train = pd.read_table(cdir + '/train.txt')['CATEGORY']
X_valid = pd.read_table(cdir + '/valid.feature.txt')
Y_valid = pd.read_table(cdir + '/valid.txt')['CATEGORY']
X_test = pd.read_table(cdir + '/test.feature.txt')
Y_test = pd.read_table(cdir + '/test.txt')['CATEGORY']

# 予測
print('train accuracy: ', accuracy_score(Y_train, lr.predict(X_train)))
print('valid accuracy: ', accuracy_score(Y_valid, lr.predict(X_valid)))
print('test accuracy: ', accuracy_score(Y_test, lr.predict(X_test)))
