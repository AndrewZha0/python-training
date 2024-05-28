# 1、while 语句，只要条件（这里指：a < 10）保持为真就会一直执行
a = 0
while a < 10:
    print(a)
    a += 1

# 2、if 语句
# 包含零个或多个 elif 子句及可选的 else 子句。关键字 'elif' 是 'else if' 的缩写，适用于避免过多的缩进
x = int(input("输入一个数字: "))
if x < 0:
    x = 0
    print('负数变为 0')
elif x == 0:
    print('0')
elif x == 1:
    print('1')
else:
    print('大于 1')

x = int(input("输入一个数字: "))
if x < 0:
    x = 0
    print('负数变为 0')
elif x == 0:
    print('0')
elif x == 1:
    print('1')
else:
    print('大于 1')

x = int(input("输入一个数字: "))
if x < 0:
    x = 0
    print('负数变为 0')
elif x == 0:
    print('0')
elif x == 1:
    print('1')
else:
    print('大于 1')

x = int(input("输入一个数字: "))
if x < 0:
    x = 0
    print('负数变为 0')
elif x == 0:
    print('0')
elif x == 1:
    print('1')
else:
    print('大于 1')

# 3、for 语句
my_list = ['张三', '李老二', '王麻美子']
for name in my_list:
    print(name, len(name))

# 4、range() 函数
# 内置函数 range() 常用于遍历数字序列，该函数可以生成算术级数，生成的序列不包含给定的终止数值
for i in range(5):
    print(i)

# range 可以不从 0 开始，还可以按指定幅度递增（递增幅度称为 '步进'，支持负数）
print(f'5 ～ 9：{list(range(5, 10))}')
print(f'0 ～ 9，步进为3：{list(range(0, 10, 3))}')
print(f'-10 ～ -100，步进为-30：{list(range(-10, -100, -30))}')

# 5、循环中的 break、continue 语句及 else 子句
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '=', x, '*', n // x)
            break
    else:
        print(n, '是一个素数')
# else 子句属于 for 循环，不属于 if 语句，在未运行 break 时执行

# continue 语句表示继续执行循环的下一次迭代
for num in range(2, 10):
    if num % 2 == 0:
        print("偶数：", num)
        continue
    print("奇数：", num)


# 6、pass 语句
# pass 语句不执行任何操作。语法上需要一个语句，但程序不实际执行任何动作时，可以使用该语句
class MyEmptyClass:
    pass


# pass 还可以用作函数或条件子句的占位符，让开发者聚焦更抽象的层次，此时，程序直接忽略 pass
def initlog(*args):
    pass


# 7、match 语句，将一个目标值与一个或多个字面值进行比较
# _ 被作为 通配符 并必定会匹配成功
# | 在一个模式中可以组合多个字面值
def http_error(status):
    match status:
        case 400 | 401:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


print(f'状态为400的异常信息为：{http_error(400)}')
print(f'状态为401的异常信息为：{http_error(401)}')
print(f'状态为404的异常信息为：{http_error(404)}')
print(f'状态为418的异常信息为：{http_error(418)}')
print(f'状态为420的异常信息为：{http_error(420)}')
