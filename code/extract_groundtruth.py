def extrct_groundtruth():
    # 构建商品子集
    item_set = []
    file = open('../data/tianchi_fresh_comp_train_item.csv')
    file.readline()
    for line in file:
        arr = line.replace('\n', '').split(',')
        item_set.append(arr[0])
    item_set = set(item_set)

    file = open('../data/31.csv')
    ground_truth = []
    for line in file:
        arr = line.replace('\n', '').split(',')
        if arr[1] in item_set and arr[2] == '4':
            ground_truth.append('%s,%s\n' % (arr[0], arr[1]))
    file.close()
    ground_truth = list(set(ground_truth))

    file = open('ground_truth.csv', 'w')
    file.write('user_id,item_id\n')
    for i in ground_truth:
        file.write(i)
    file.close()
