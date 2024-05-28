from collections import Counter
from collections import defaultdict
import csv


# Counter
# def read_portfolio(filename):
#     portfolio = Counter()
#     with open(filename, encoding='UTF-8-sig') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             d = dict(zip(headers, row))
#             portfolio[d['Name']] += int(d['Shards'])
#     return portfolio
def read_portfolio(filename):
    portfolio = defaultdict(list)
    with open(filename, encoding='UTF-8-sig') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            d = dict(zip(headers, row))
            portfolio[d['Name']].append(int(d['Shards']))
    return portfolio


if __name__ == '__main__':
    portfolio = read_portfolio('../../data/portfolio1.csv')
    print(portfolio)
