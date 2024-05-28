import numpy as np

data = np.array([
    [80, 200],
    [95, 230],
    [104, 245],
    [112, 274],
    [125, 259],
    [135, 262],
])

m = 1
b = 1
weight = np.array([[m], [b]])
feature = data[:, 0:1]
feature_matrix = np.append(feature, np.ones(shape=(len(feature), 1)), axis=1)
label = np.expand_dims(data[:, -1], axis=1)
learning_rate = 0.00001


def gradient_descent():
    result = np.dot(feature_matrix.T, np.dot(feature_matrix, weight) - label) / len(feature) * 2
    print(result)
    return result


def train():
    global weight
    for i in range(1, 10000000):
        result = gradient_descent()
        weight = weight - result * learning_rate
        if abs(result[0][0]) < 0.5 and abs(result[1][0]) < 0.5:
            break
    print("weight={}".format(weight))


if __name__ == '__main__':
    train()
