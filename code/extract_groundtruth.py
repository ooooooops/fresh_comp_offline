def extrct_groundtruth():
    file = open('../data/31.csv')
    ground_truth = []
    for line in file:
        arr = line.replace('\n', '').split(',')
        if arr[2] == '4':
            ground_truth.append('%s,%s\n' % (arr[0], arr[1]))
    file.close()
    ground_truth = list(set(ground_truth))

    file = open('ground_truth.csv', 'w')
    file.write('user_id,item_id\n')
    for i in ground_truth:
        file.write(i)
    file.close()
