import feat_extract as fe
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import numpy as np


def train():
    models = []
    weights = []
    for span in range(1, 8):
        feats, labels, weight = fe.extract_feature(span)
        print("extract %d features while span is %d" % (len(feats), span))
        # print('weight is %f' % weight)
        weights.append(weight)
        X = np.mat(feats)
        y = np.array(labels).T
        print(np.shape(y))
        print(y)
        model = LogisticRegression()
        # model = DecisionTreeClassifier()
        # model = RandomForestClassifier()
        # model.predict_proba()
        model.fit(X, y)
        models.append(model)
        # break
    return models, weights

#train()
