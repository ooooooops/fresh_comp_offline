#!usr/bin/env python
# coding=utf-8

import numpy as np

# f = open('tianchi_fresh_comp_train_user.csv')
# context = f.readlines()

train_day29 = []  # user item pairs of day 29
offline_day30 = []
online_day31 = []

file = 'tianchi_fresh_comp_train_user.csv'
f = open(file)
f.readline()
for line in f:
    line = line.replace('\n', '')
    arr = line.split(',')
    day = arr[-1].split(' ')[0]
    uid = (arr[0], arr[1])
    if day == '2014-12-17':
        train_day29.append(uid)
    elif day == '2014-12-18':
        offline_day30.append(uid)

f.close()

train_day29 = list(set(train_day29))
offline_day30 = list(set(offline_day30))
# online_day31 = list(set(online_day31))

import math

uid_dict = [{} for i in range(4)]
f.open(file)
f.readline()
for line in f:
    line = line.replace('\n', '')
    arr = line.split(',')
    uid = [arr[0], arr[1], arr[-1]]
    op = int(arr[2])-1
    if uid in uid_dict[op]:
        uid_dict[op][uid] += 1
    else:
        uid_dict[op][uid] = 1
f.close()

ui_buy = {}
f.open(file)
f.readline()
for line in f:
    line = line.replace('\n', '')
    arr = line.split(',')
    uid = [arr[0], arr[1], arr[-1]]
    if arr[2] == '4':
        ui_buy[uid] = 1
f.close()
##  step 1. 1-->4  
X = np.zeros((len(train_day29), 4))
y = np.zeros((len(train_day29)), )
id = 0
for uid in train_day29:
    last_ui = (uid[0], uid[1], uid[2])
    for i in range(4):
        X[id][i] = math.log1p(train_day29[i][uid] if uid in train_day29[i] else 0)
    y[id] = 1 if uid in ui_buy else 0
    id += 1
print('X = ', X, '\n\n', 'y = ', y)
print('-----------------------------------\n\n')

pX = np.zeros((len(ui30), 4))
id = 0
for ui in ui30:
    # last_ui = (uid[0], uid[1], uid[2])
    for i in range(4):
        pX[id][i] = math.log1p(offline_day30[i][ui] if ui in offline_day30[i] else 0)
    id += 1

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
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

lx = zip(ui30, py)
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
