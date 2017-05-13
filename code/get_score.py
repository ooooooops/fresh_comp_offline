#!usr/bin/env python
# coding=utf-8

import sys


def get_score():
    ground_truth = []
    gt = open('ground_truth.csv')
    gt.readline()
    for line in gt:
        arr = line.replace('\n', '')
        ground_truth.append(arr)
    ground_truth = set(ground_truth)

    pred_ans = []
    pred_ans_file = open('ans.csv')
    pred_ans_file.readline()
    for line in pred_ans_file:
        arr = line.replace('\n', '')
        pred_ans.append(arr)
    pred_ans = set(pred_ans)

    inter = ground_truth & pred_ans
    print('hit number:', len(inter))
    if len(inter) > 0:
        a = len(ground_truth)
        b = len(pred_ans)
        c = len(inter)
        P = 1.0 * c / b * 100
        R = 1.0 * c / a * 100
        F1 = 2.0 * R * P / (R + P)
        print('n_ground_truth:%d,n_pred_ans:%d,inter:%d' % (a,b,c) )
        print('F1/P/R %.2f%%/%.2f%%/%.2f%%\n' % (F1, P, R))
