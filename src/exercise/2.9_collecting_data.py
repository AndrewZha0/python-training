def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        next(f)
        for i, row in enumerate(f):
            row = row.replace('\n', '')[1:-1].replace('""', '').split(',')
            t = (row[0], int(row[1]), float(row[2]), 0.8 * float(row[2]))
            portfolio.append(t)
    return portfolio


if __name__ == '__main__':
    portfolio = read_portfolio('../../data/portfolio.csv')
    # print(portfolio)
    print('%10s %10s %10s %10s' % ('Name', 'Shares', 'Price', 'Change'))
    for t in portfolio:
        print('%10s %10d %10.2f %10.2f' % t)
