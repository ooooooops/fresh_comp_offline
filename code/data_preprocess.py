# -*- coding=utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib
# 统计31天中每一天的4种操作数
statitic = [[0, 0, 0, 0] for i in range(31)]
for i in range(31):
    file = open('../data/%s.csv' % (i+1))
    print("process day %s..." % (i+1))
    for line in file:
        arr = line.replace('\n', '').split(',')
        op = int(arr[2]) - 1
        statitic[i][op] += 1
    file.close()

# 画出折线图
yahei = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
titles = ['浏览', '收藏', '加购物车', '购买']
x = [i for i in range(1, 32)]
y = [i for i in range(31)]
for i in range(4):
    for j in range(31):
        y[j] = statitic[j][i]
    plt.figure()
    plt.plot(x, y)
    plt.title(titles[i], fontproperties=yahei)
    plt.savefig(u"%s.png" % titles[i])
