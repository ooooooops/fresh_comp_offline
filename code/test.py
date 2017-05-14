import train
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import os
import time
import get_score


def frange(x, y, jump):
    while x < y:
        yield x
        x += jump


def test(thresh=0.1):
    models = []
    weights = []
    ui_probs = {}
    if os.path.exists('models.npz'):
        models_file = np.load('models.npz')
        models = models_file['arr_0']
        weights = models_file['arr_1']
    else:
        print('training models...')
        time1 = time.time()
        models, weights = train.train()
        time2 = time.time()
        # models = np.array(models)
        # weights = np.array(weights)
        print('train models cost %ds' % (time2 - time1))
        np.savez('models.npz', models, weights)
        print('training models...done')
    if type(weights) == list:
        weights = np.array(weights)
    weights = weights / weights.sum()
    print(weights)
    for span in range(1, 8):
        file = open('../data/%d.csv' % (32 - span))
        print("predict %d day before day31" % span)
        feat_set = {}
        for line in file:
            arr = line.replace('\n', '').split(',')
            ui = arr[0] + ',' + arr[1]
            op = int(arr[2]) - 1
            if ui in feat_set.keys():
                feat_set[ui][op] += 1
            else:
                feat_set[ui] = [0, 0, 0, 0]
                feat_set[ui][op] += 1

        ui_set = []
        feats = []
        for (ui, feat) in feat_set.items():
            ui_set.append(ui)
            feats.append(feat)

        model = models[span - 1]
        # print(type(models))
        # print(models)
        # print(type(model))
        # print(model)
        weight = weights[span - 1]
        # print(models)
        # print(weights)
        pX = np.mat(feats)
        py = model.predict_proba(pX)
        npy = []
        for a in py:
            npy.append(a[1] * weight)
        py = npy

        for i in range(len(ui_set)):
            ui = ui_set[i]
            prob = py[i]
            if ui in ui_probs.keys():
                ui_probs[ui] += prob
                # print(prob)
            else:
                ui_probs[ui] = prob
                # ui_probs[ui] += prob
    ui_probs = sorted(ui_probs.items(), key=lambda x: x[1], reverse=True)

    # 构建商品子集
    item_set = []
    file = open('../data/tianchi_fresh_comp_train_item.csv')
    file.readline()
    for line in file:
        arr = line.replace('\n', '').split(',')
        item_set.append(arr[0])
    item_set = set(item_set)
    #for thresh in frange(0.1, 0.9, 0.1):
        #print('thresh:%f' % thresh)
    wf = open('ans.csv', 'w')
    wf.write('user_id,item_id\n')
    for item in ui_probs:
        if item[1] >= 0.2:  # config
            if item[0].split(',')[1] in item_set:
                wf.write("%s\n" % item[0])
        else:
            break
    wf.close()
        #get_score.get_score()
'''
    wf = open('cache.txt', 'w')
    wf.write('user_id,item_id\n')
    for item in ui_probs:
        wf.write("%s,%s\n" % (item[0], item[1]))
    wf.close()
'''