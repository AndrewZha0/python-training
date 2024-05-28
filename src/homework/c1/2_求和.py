def reverse_and_sum(n):
    sum_of_digits = 0
    reversed_str = str(n)[::-1]
    print("逆序输出的各位数:")
    for digit in reversed_str:
        print(digit, end='')
        # 累加每一位数
        sum_of_digits += int(digit)
    print("\n各位数之和为:", sum_of_digits)


try:
    number = int(input("请输入一个整数: "))
    reverse_and_sum(number)
except ValueError:
    print("输入的不是一个有效的整数，请重新输入。")
