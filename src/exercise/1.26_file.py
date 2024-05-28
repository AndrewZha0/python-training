# with open('../../data/portfolio.csv', 'rt') as f:
#     for line in f:
#         print(line, end='')

# f = open('../../data/portfolio.csv', 'rt')
# headers = next(f)
# print(headers)
# for line in f:
#     print(line, end='')
# f.close()

# f = open('../../data/portfolio.csv', 'rt', encoding='utf-8')
# headers = next(f).split(',')
# print(headers)
# for line in f:
#     row = line.split(',')
#     print(row)
# f.close()

# 1.28
f = open('../../data/portfolio1.csv', 'rt')
headers = next(f)
sumPrice = 0
for line in f:
    row = line.replace('\n', '').split(',')
    sumPrice += int(row[1]) * float(row[2])
f.close()
print(f'Total cost {sumPrice}')

