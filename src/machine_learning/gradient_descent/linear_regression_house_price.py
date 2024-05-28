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
x_array = data[:, 0]
y_array = data[:, -1]

learning_rate = 0.00001


def gradient_descent():
    m_slop = 0
    for i, x in enumerate(x_array):
        m_slop = m_slop + x * (m * x + b - y_array[i])
    m_slop = m_slop * 2 / len(x_array)
    b_slop = 0
    for i, x in enumerate(x_array):
        b_slop = b_slop + m * x + b - y_array[i]
    b_slop = b_slop * 2 / len(x_array)
    print("mse对m求导={}".format(m_slop))
    print("mse对b求导={}".format(b_slop))
    return m_slop, b_slop


def train():
    global m
    global b
    for i in range(1, 10000000):
        m_slop, b_slop = gradient_descent()
        b = b - b_slop * learning_rate
        m = m - m_slop * learning_rate
        if abs(b_slop) < 0.5 and abs(m_slop) < 0.5:
            break
    print("m={},b={}".format(m, b))


if __name__ == '__main__':
    train()
