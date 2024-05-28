def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("输入必须是非负整数。")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


try:
    number = int(input("请输入一个非负整数来计算其阶乘: "))
    result = factorial(number)
    print(f"{number}的阶乘为: {result}")
except ValueError as e:
    print(e)
