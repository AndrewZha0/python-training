my_list = ['张三', '李四', '王五']

# 查找某元素在列表内的下标索引
index = my_list.index('李四')
print(f'李四在列表中的下标是：{index}')

# 被查找的元素不存在，会报错 [ValueError: '赵六' is not in list]
# index = my_list.index('赵六')
# print(f'赵六在列表中的下标是：{index}')

my_list = ['张三', '李四', '王五']
# 修改特定下标索引的值
my_list[1] = '杨过'
print(f'修改后的结果是：{my_list}')

my_list = ['张三', '李四', '王五']
# 在指定下标位置插入新元素
my_list.insert(1, '小龙女')
print(f'插入新元素后的结果是：{my_list}')

my_list = ['张三', '李四', '王五']
# 在列表的尾部追加单个元素
my_list.append('欧阳锋')
print(f'追加单个元素后的结果：{my_list}')

my_list = ['张三', '李四', '王五']
# 在列表尾部追加多个元素（新列表）
new_list = ['郭靖', '黄蓉']
my_list.extend(new_list)
print(f'追加多个元素后的结果：{my_list}')

# 删除指定下标的元素（一）
my_list = ['张三', '李四', '王五']
del my_list[1]
print(f'删除元素后的结果是：{my_list}')

# 删除指定下标的元素（二）
my_list = ['张三', '李四', '王五']
pop = my_list.pop(1)
print(f'删除元素后的结果是：{my_list}，删除的元素是：{pop}')

# 删除某元素在列表中的第一个匹配项
my_list = ['张三', '李四', '张三', '李四', '王五']
my_list.remove('李四')
print(f'删除元素后的结果是：{my_list}')

# 清空列表
my_list = ['张三', '李四', '王五']
my_list.clear()
print(f'清空元素后的结果是：{my_list}')

# 统计某个元素的数量
my_list = ['张三', '李四', '张三', '李四', '王五']
count = my_list.count('李四')
print(f'列表中李四的数量是：{count}')

# 统计全部元素的数量
my_list = ['张三', '李四', '王五']
count = len(my_list)
print(f'列表中所有元素的数量是：{count}')

# 排序
my_list = [3, 5, 2, 4, 1, 6]
my_list.sort()
print(f'排序后的列表是：{my_list}')

# while循环遍历列表
my_list = ['张三', '李四', '王五']
index = 0
while index < len(my_list):
    print(f'列表元素：{my_list[index]}')
    index += 1

# for循环遍历列表
my_list = ['张三', '李四', '王五']
for item in my_list:
    print(f'列表元素：{item}')
