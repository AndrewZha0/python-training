from pprint import pprint


def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        next(f)
        for i, row in enumerate(f):
            row = row.replace('\n', '')[1:-1].replace('""', '').split(',')
            d = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(d)
    return portfolio


if __name__ == '__main__':
    portfolio = read_portfolio('../../data/portfolio.csv')
    total = 0.0
    for s in portfolio:
        total += s['shares'] * s['price']
    pprint(portfolio)
    print(total)
