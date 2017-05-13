#!usr/bin/env python
# coding=utf-8

import numpy as np

f = open('tianchi_fresh_comp_train_user.csv')
context = f.readlines()

train_day29 = []  # user item day pairs of day 29
offline_day30 = []
online_day31 = []

for line in context:
    line = line.replace('\n', '')
    arr = line.split(',')
    if arr[0] == 'user_id':
        continue
    day = arr[-1]
    uid = (arr[0], arr[1], day+1)
    if day == 28:
        train_day29.append(uid)
    if day == 29:
        offline_day30.append(uid)
    if day == 30:
        online_day31.append(uid)

train_day29 = list(set(train_day29))
offline_day30 = list(set(offline_day30))
online_day31 = list(set(online_day31))

import math

# 按照操作类型分类统计
uid_dict = [{} for i in range(4)]
for line in context:
    line = line.replace('\n', '')
    arr = line.split(',')
    if arr[0] == 'user_id':
        continue
    day = int(arr[-1])-1
    uid = [arr[0], arr[1], day]
    type = int(arr[2]) - 1
    if uid in uid_dict[type]:
        uid_dict[type][uid] += 1
    else:
        uid_dict[type][uid] = 1
f.close()

ui_buy = {}
for line in context:
    line = line.replace('\n', '')
    arr = line.split(',')
    if arr[0] == 'user_id':
        continue
    uid = [arr[0], arr[1], int(arr[-1])]
    if arr[2] == '4':
        ui_buy[uid] = 1

##  step 1. 1-->4
X = np.zeros((len(train_day29), 4))
y = np.zeros((len(train_day29)), )
id = 0
for uid in train_day29:
    last_ui = (uid[0], uid[1], uid[2] - 1)
    for i in range(4):
        X[id][i] = math.log1p(train_day29[i][uid] if uid in train_day29[i] else 0)
    y[id] = 1 if uid in ui_buy else 0
    id += 1
print('X = ', X, '\n\n', 'y = ', y)
print('-----------------------------------\n\n')

pX = np.zeros((len(offline_day30), 4))
id = 0
for ui in offline_day30:
    last_ui = (uid[0], uid[1], uid[2] - 1)
    for i in range(4):
        pX[id][i] = math.log1p(offline_day30[i][ui] if ui in offline_day30[i] else 0)
    id += 1

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

# from sklearn.tree import DecisionTreeClassifier
# model = DecisionTreeClassifier(max_depth=4)
# from sklearn.ensemble import RandomForestClassifier
# model = RandomForestClassifier()

model.fit(X, y)

py = model.predict_proba(pX)
npy = []
for a in py:
    npy.append(a[1])
py = npy

print('pX = ')
print(pX)
# print ('y = ')
# print (py)

lx = zip(offline_day30, py)
print(lx)
print('-----------------------------------\n')
lx = sorted(lx, key=lambda x: x[1], reverse=True)
print(lx)
print('-----------------------------------\n')

wf = open('ans.csv', 'w')
wf.write('user_id,item_id\n')
for i in range(437):
    item = lx[i]
    wf.write('%s,%s\n' % (item[0][0], item[0][1]))
