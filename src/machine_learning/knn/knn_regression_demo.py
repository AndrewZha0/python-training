import numpy as np

feature = np.array([
    [-121, 47, 33],
    [-121.2, 46.7, 33],
    [-122, 46.3, 32],
    [-120.9, 46.7, 32],
    [-120.1, 46.2, 34]
])

label = np.array([200, 210, 250, 215, 232])

predict_point = np.array([-121, 46, 32])
# 欧氏距离
# 矩阵相减，求平方
matrix_temp = np.square(feature - predict_point)
# 逐行相加，开平方，排序下标
sorted_index = np.argsort(np.sqrt(np.sum(matrix_temp, axis=1)))

sorted_label = label[sorted_index]

# 取前k个label，求平均值
k = 3
predict_price = np.sum(sorted_label[0:k]) / k
print("预测的房价是{}万。".format(predict_price))
