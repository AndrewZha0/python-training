with open('../../data/portfolio.csv', 'rt') as f:
    next(f)
    for i, row in enumerate(f):
        row = row.replace('\n', '')[1:-1].replace('""', '').split(',')
        t = (row[0], int(row[1]), float(row[2]))
        cost = t[1] * t[2]
        print(f'row {i} cost: {cost:0.2f}')
