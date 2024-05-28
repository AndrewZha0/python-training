import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename, encoding='UTF-8-sig') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            d = dict(zip(headers, row))
            portfolio.append(d)
    return portfolio


if __name__ == '__main__':
    portfolio = read_portfolio('../../data/portfolio1.csv')
    print(portfolio)
    l = [s for s in portfolio if int(s['Shards']) > 100]
    print(l)
