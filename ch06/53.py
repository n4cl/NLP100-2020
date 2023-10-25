import os
import pickle
import numpy as np
import pandas as pd

cdir = os.path.dirname(os.path.abspath(__file__))

# モデルの読み込み
def load_model():
    with open(cdir + '/model.pickle', mode='rb') as f:
        model = pickle.load(f)
    return model

lr = load_model()

# データの読み込み
X_test = pd.read_table(cdir + '/test.feature.txt')

# 予測
Y_pred = lr.predict(X_test)
Y_pred_p = np.max(lr.predict_proba(X_test), axis=1)

# 結果の出力
for yp, ypp in zip(Y_pred, Y_pred_p):
    print(yp, ypp)
