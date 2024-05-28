import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename, encoding='UTF-8-sig') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            print('----------------------------')
            print(list(zip(headers, row)))
            print(dict(zip(headers, row)))
    return portfolio


if __name__ == '__main__':
    read_portfolio('../../data/portfolio1.csv')
