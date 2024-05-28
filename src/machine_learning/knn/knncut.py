import numpy as np

data = np.loadtxt("fileName", delimiter=",")
np.random.shuffle(data)

test_data = data[0:100]
train_data = data[100:-1]

np.savetxt("test_data.csv", test_data, fmt="%d", delimiter=",")
np.savetxt("train_data.csv", train_data, fmt="%d", delimiter=",")
