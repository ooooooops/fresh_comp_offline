#!usr/bin/env python
# coding=utf-8

import sys


ground_truth = []
for line in open('tianchi_fresh_comp_train_user.csv'):
    line = line.replace('\n', '')
    arr = line.split(',')
    if arr[0] == 'user_id':
        continue
    time = arr[-1].split(' ')[0]
    if time == '2014-12-17' and arr[2] == '4':
        ground_truth.append(arr[0]+','+arr[1])

ground_truth = set(ground_truth)


pred_ans_file = open('ans.csv')
# t = pred_ans_file.readlines()
pred_ans = []
for line in pred_ans_file.readlines():
    if line[0] == 'u':
        continue
    line = line.replace('\n','')
    pred_ans.append(line)
pred_ans = set(pred_ans)

inter = ground_truth & pred_ans
print('hit number:', len(inter))
if len(inter) > 0:
    a = len(ans)
    b = len(ans_)
    c = len(inter)
    P = 1.0 * c / b * 100
    R = 1.0 * c / a * 100
    F1 = 2.0 * R * P / (R + P)
    print('n_ans:%d,n_ans_:%d,inter:%d' % (a,b,c) )
    print('F1/P/R %.2f%%/%.2f%%/%.2f%%\n' % (F1, P, R))
