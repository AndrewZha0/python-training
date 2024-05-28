# def greeting(name):
#     'Issues a greeting'
#     print('Hello', name)
#
#
# greeting('andrew')


# 1.30
# def portfolio_cost(filename):
#     f = open(filename, 'rt')
#     headers = next(f)
#     sumPrice = 0
#     for line in f:
#         row = line.replace('\n', '').split(',')
#         sumPrice += int(row[1]) * float(row[2])
#     f.close()
#     return sumPrice
#
#
# cost = portfolio_cost('../../data/portfolio1.csv')
# print('Total cost:', cost)


# 1.32
import csv

f = open('../../data/portfolio1.csv')
rows = csv.reader(f)
headers = next(rows)
print(headers)
for row in rows:
    print(row)
f.close()
