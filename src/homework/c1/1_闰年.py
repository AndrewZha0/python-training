def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


year_input = input("请输入一个年份: ")
try:
    year = int(year_input)
    if is_leap_year(year):
        print(f"{year}年是闰年。")
    else:
        print(f"{year}年不是闰年。")
except ValueError:
    print("输入的年份不是一个有效的整数，请重新输入。")
