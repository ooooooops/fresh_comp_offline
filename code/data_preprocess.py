# -*- coding=utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib

# 统计31天中每一天的4种操作数
# statitic = [[0, 0, 0, 0] for i in range(31)]
# for i in range(31):
#     file = open('../data/%s.csv' % (i+1))
#     print("process day %s..." % (i+1))
#     for line in file:
#         arr = line.replace('\n', '').split(',')
#         op = int(arr[2]) - 1
#         statitic[i][op] += 1
#     file.close()

# 画出折线图
# yahei = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
# titles = ['浏览', '收藏', '加购物车', '购买']
# x = [i for i in range(1, 32)]
# y = [i for i in range(31)]
# for i in range(4):
#     for j in range(31):
#         y[j] = statitic[j][i]
#     plt.figure()
#     plt.plot(x, y)
#     plt.title(titles[i], fontproperties=yahei)
#     plt.savefig(u"%s.png" % titles[i])

# 清理不在商品子集中的商品
# 构建商品子集
# item_set = []
# file = open('../data/tianchi_fresh_comp_train_item.csv')
# file.readline()
# for line in file:
#     arr = line.replace('\n', '').split(',')
#     item_set.append(arr[0])
# item_set = set(item_set)
#
# # 开始清理
# for i in range(31):
#     file = open('../data/%s.csv' % (i + 1))
#     print("process day %s..." % (i + 1))
#     lines = []
#     cnt = 0
#     for line in file:
#         cnt += 1
#         arr = line.replace('\n', '').split(',')
#         if arr[1] in item_set:
#             lines.append(line)
#     file.close()
#     file = open('../data/%s.csv' % (i + 1), 'w')
#     for line in lines:
#         file.write(line)
#     file.close()
#     print('there are %d items is not in commodity subset.' % (cnt - len(lines)))
