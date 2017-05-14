import numpy


def extract_feature(days_span):
    print('extract_feature:days_span=%d' % days_span)
    feat_set = []
    labels = []
    buy_count = 0
    for day in range(1, 32-days_span):  # config
        if day == 25:  # config
            continue
        file = open('../data/%d.csv' % day)
        print('extracting features from file ../data/%d.csv' % day)
        user2feat = {}
        for line in file:
            arr = line.replace('\n', '').split(',')
            key_ui = arr[0]+','+arr[1]
            feat = [0, 0, 0, 0]
            if key_ui in user2feat.keys():
                user2feat[key_ui][int(arr[2]) - 1] += 1
            else:
                user2feat[key_ui] = [0, 0, 0, 0]
                user2feat[key_ui][int(arr[2]) - 1] += 1
        file.close()

        file2 = open('../data/%d.csv' % (day+days_span))
        print('extracting labels from file ../data/%d.csv' % (day+days_span))
        ui_buy = []
        for line in file2:
            arr = line.replace('\n', '').split(',')
            ui = arr[0]+','+arr[1]
            # op = int(arr[2])
            if arr[2] == '4':
                ui_buy.append(ui)
        ui_buy = set(ui_buy)
        # print(ui_buy)
        file2.close()

        for (ui, feat) in user2feat.items():
            feat_set.append(feat)
            if ui in ui_buy:
                labels.append(1)
                buy_count += 1
            else:
                labels.append(0)
        # break
    feat_set = numpy.log1p(feat_set)
    return feat_set, labels, float(buy_count) / float(len(labels))
