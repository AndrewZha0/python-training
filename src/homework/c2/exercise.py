s = ('GOOG', 100, 490.1)
name = s[0]  # 'GOOG'
shares = s[1]  # 100
price = s[2]  # 490.1

s1 = {
    'name': 'GOOG',
    'shares': 100,
    'price': 490.1
}
print(s['name'], s['shares'])

d = {
    'name': row[0],
    'shares': int(row[1]),
    'price': float(row[2])
}
cost = d['shares'] * d['price']
d['shares'] = 75
d['date'] = (6, 11, 2007)
d['account'] = 12345
list(d)
for k in d:
    print('k =', k)

for k in d:
    print(k, '=', d[k])

keys = d.keys()
items = d.items()
for k, v in d.items():
    print(k, '=', v)

d = dict(items)
print(d)

# String
symbols = 'AAPL,IBM,MSFT,YHOO,SCO'
print(symbols[0])
print(symbols[1])
print(symbols[2])
print(symbols[-1])
print(symbols[-2])
print('IBM' in symbols)
print(symbols.lower())
print(symbols)

# number
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment

print('Total paid', total_paid)

# container
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
my_list = [
    '张三',
    '李四',
    '张三',
    '李四',
    '王五'
]
count = my_list.count('李四')
print(f'列表中李四的数量是：{count}')

# 统计全部元素的数量
my_list = [
    '张三',
    '李四',
    '王五'
]
count = len(my_list)
print(f'列表中所有元素的数量是：{count}')

# 排序
my_list = [
    3,
    5,
    2,
    4,
    1,
    6
]
my_list.sort()
print(f'排序后的列表是：{my_list}')

# while循环遍历列表
my_list = [
    '张三',
    '李四',
    '王五'
]
index = 0
while index < len(my_list):
    print(f'列表元素：{my_list[index]}')
    index += 1

# for循环遍历列表
my_list = ['张三', '李四', '王五']
for item in my_list:
    print(f'列表元素：{item}')

# 元组由多个用逗号隔开的值组成
# 输入时，圆括号可有可无，不过经常是必须的
my_tuple = '张三', '李四', '王五'
# 输出时，元组都要由圆括号标注，这样才能正确地解释嵌套元组
print(my_tuple)

# 元组是 immutable （不可变的），一般可包含异质元素序列，通过解包或索引访问（如果是 namedtuples，可以属性访问）
# 列表是 mutable （可变的），列表元素一般为同质类型，可迭代访问

# 构造 0 个元素的元组（一对空圆括号）
empty = ()
print(empty)
# 构造 1 个元素的元组（在这个元素后添加逗号）
singleton = '小明',
print(singleton)

# 元组打包
t = 100, True, '小明'
# 序列解包，左侧变量与右侧序列元素的数量应相等
x, y, z = t
print(t)
print(x)
print(y)
print(z)

# 集合是由不重复元素组成的无序容器
# 创建集合用花括号或 set() 函数
# 创建空集合只能用 set()，不能用 {}，{} 创建的是空字典
my_collect = {'张三', '李四', '王五'}
print(my_collect)

# 成员检测
print('张三' in my_collect)
print('李四' not in my_collect)

a = set('aabb')
b = set('aacc')
# 去重
print(a)
print(b)
# 差集
print(a - b)
print(b - a)
# 合集
print(a | b)
# 交集
print(a & b)
# 不在a中 或者 不在b中
print(a ^ b)

portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.3),
    ('CAT', 150, 83.44)
]
print(portfolio[0])
print(portfolio[2])

records1 = []
records1.append(('GOOG', 100, 490.10))
records1.append(('IBM', 50, 91.3))

prices = {
    'GOOG': 513.25,
    'CAT': 87.22,
    'IBM': 93.37,
    'MSFT': 44.12
}
print(prices['IBM'])
print(prices['GOOG'])

prices = {}  # Initial empty dict

# Insert new items
prices['GOOG'] = 513.25
prices['CAT'] = 87.22
prices['IBM'] = 93.37

holidays = {
    (1, 1): 'New Years',
    (3, 14): 'Pi day',
    (9, 13): "Programmer's day",
}

print(holidays[3, 14])

names = [
    'IBM',
    'AAPL',
    'GOOG',
    'IBM',
    'GOOG',
    'YHOO'
]
unique = set(names)
unique.add('CAT')  # Add an item
unique.remove('YHOO')

portfolio = [
    ('AA', 100, 32.2),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('MSFT', 200, 51.23),
    ('GE', 95, 40.37),
    ('MSFT', 50, 65.1),
    ('IBM', 100, 70.44)
]

print(portfolio[0])
print(portfolio[1])

print(portfolio[1][1])

total = 0.0
for s in portfolio:
    total += s[1] * s[2]

print(total)

total = 0.0
for name, shares, price in portfolio:
    total += shares * price

print(total)

portfolio = [
    {'name': 'AA', 'shares': 100, 'price': 32.2},
    {'name': 'IBM', 'shares': 50, 'price': 91.1},
    {'name': 'CAT', 'shares': 150, 'price': 83.44},
    {'name': 'MSFT', 'shares': 200, 'price': 51.23},
    {'name': 'GE', 'shares': 95, 'price': 40.37},
    {'name': 'MSFT', 'shares': 50, 'price': 65.1},
    {'name': 'IBM', 'shares': 100, 'price': 70.44}
]

print(portfolio[0])
print(portfolio[1])

print(portfolio[1]['shares'])

total = 0.0
for s in portfolio:
    total += s['shares'] * s['price']

print(total)
