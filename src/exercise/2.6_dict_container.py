def read_portfolio(filename):
    portfolio = {}
    with open(filename, 'rt') as f:
        next(f)
        for i, row in enumerate(f):
            row = row.replace('\n', '')[1:-1].replace('""', '').split(',')
            portfolio[row[0]] = float(row[2])
    return portfolio


if __name__ == '__main__':
    portfolio = read_portfolio('../../data/portfolio.csv')
    print(portfolio)
    print(portfolio['IBM'])
