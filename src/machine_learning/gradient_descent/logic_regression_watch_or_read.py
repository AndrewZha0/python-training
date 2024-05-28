import numpy as np

data = np.array([
    [5, 0], [15, 0], [25, 1], [35, 1], [45, 1], [55, 1]
])

m = 1
b = 1
weight = np.array([
    [m], [b]
])
learning_rate = 0.001

feature = data[:, 0:1]
label = data[:, -1:]
feature_matrix = np.append(feature, np.ones(shape=(6, 1)), axis=1)


def gradient_decent():
    predict = 1 / (1 + np.exp(-np.dot(feature_matrix, weight)))
    return np.dot(feature_matrix.T, predict - label)


def train():
    for i in range(1, 1000000):
        slop = gradient_decent()
        global weight
        weight = weight - learning_rate * slop
    print(weight)


if __name__ == '__main__':
    train()
