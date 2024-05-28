def countdown(n):
    while n > 0:
        yield n
        n -= 1


if __name__ == '__main__':
    for i in countdown(10):
        print(i, end=' ')
