#!usr/bin/env python
# coding=utf-8

#step 1.清洗没有行为的用户
##f = open('tianchi_fresh_comp_train_user.csv')
##w = open('data1.csv', 'w')
##w.write(f.readline())
##for line in f:
##    arr = line.replace('\n','').split(',')
##    if arr[2] != '':
##        w.write(line)
##        
##f.close()
##w.close()

#step 2.清洗没有购买或者浏览购买比过大的用户
##f = open('tianchi_fresh_comp_train_user.csv')
##w = open('data2.csv', 'w')
##w.write(f.readline())
##ui_dict = {}
##for line in f:
##    arr = line.replace('\n','').split(',')
##    ui = (arr[0], arr[1])
##    if arr[2] == '1':
##        if ui in ui_dict:
##            ui_dict[ui][0] = ui_dict[ui][0] + 1
##        else:
##            ui_dict[ui] = [0,0,0]
##    elif arr[2] == '4':
##        if ui in ui_dict:
##            ui_dict[ui][1] = ui_dict[ui][1] + 1
##        else:
##            ui_dict[ui] = [0,0,0]
##f.close()
##
##for (k,v) in ui_dict.items():
##    if 0 == v[1] or v[0]/v[1] > 2000:
##        ui_dict[k][2] = 1
##
##for line in open('tianchi_fresh_comp_train_user.csv'):
##    arr = line.replace('\n','').split(',')
##    ui = (arr[0], arr[1])
##    if ui in ui_dict and ui_dict[ui][2] == 0:
##        w.write(line)
##w.close()

#step 3.提取商品子集
f = open('data3.csv')
f1 = open('tianchi_fresh_comp_train_item.csv')
w = open('data4.csv', 'w')
item_set = set()
for line in f1:
    item_set.add(line.split(',')[0])
for line in f:
    if line.split(',')[1] in item_set:
        w.write(line)
