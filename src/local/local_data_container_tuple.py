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
