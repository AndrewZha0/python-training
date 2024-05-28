import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        next(f)
        for i, row in enumerate(f):
            row = row.replace('\n', '')[1:-1].replace('""', '').split(',')
            t = (row[0], int(row[1]), float(row[2]))
            portfolio.append(t)
    return portfolio


if __name__ == '__main__':
    portfolio = read_portfolio('../../data/portfolio.csv')
    total = 0.0
    # for s in portfolio:
    #     total += s[1] * s[2]
    for name, shards, price in portfolio:
        total += shards * price

    print(portfolio)
    print(total)
