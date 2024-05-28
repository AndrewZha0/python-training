import numpy as np
import collections


def knn(feature, label, k, predict_point):
    # 计算每个投掷点离predictPoint的距离
    distance = list(map(lambda x: abs(predict_point - x), feature))
    # 对distance的集合元素从小到大排序（返回下标）
    sorted_index = np.argsort(distance)
    # 用排序的sortedIndex来操作label集合
    sorted_label = label[sorted_index]
    # knn算法的k取最近的三个邻居
    return collections.Counter(sorted_label[0:k]).most_common(1)[0][0]


if __name__ == '__main__':
    # data = np.array([[154, 1], [126, 2], [70, 2], [196, 2], [161, 2], [371, 4]])
    # data = np.loadtxt("fileName", delimiter=",")
    train_data = np.loadtxt("train_data.csv", delimiter=",")
    # 输入值
    feature = train_data[:, 0]
    # 结果值
    label = train_data[:, -1]
    # # 预测点
    # predictPoint = 200
    # k = 3
    # result = exe(feature, label, k, predictPoint)
    # print(result)

    test_data = np.loadtxt("test_data.csv", delimiter=",")
    for k in range(1, 50):
        count = 0
        for item in test_data:
            predict = knn(feature, label, k, item[0])
            real = item[1]
            if predict == real:
                count += 1
        print("k={}, 准确率:{}%".format(k, count * 100 / len(test_data)))
