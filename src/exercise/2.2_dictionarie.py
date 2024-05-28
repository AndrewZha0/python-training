with open('../../data/portfolio.csv', 'rt') as f:
    next(f)
    for i, row in enumerate(f):
        row = row.replace('\n', '')[1:-1].replace('""', '').split(',')
        d = {
            'name': row[0],
            'shares': int(row[1]),
            'price': float(row[2])
        }
        cost = d['shares'] * d['price']
        d['date'] = (6, 11, 2007)
        d['cost'] = round(cost, 2)
        # print(f'row {i} cost: {cost:0.2f}')

        # print(f'-------- row {i} -------------')
        # for k in d:
        #     print(k, '=', d[k])

        # keys = d.keys()
        # print(keys)

        # items = d.items()
        # print(f'-------- row {i} -------------')
        # for k, v in items:
        #     print(k, '=', v)

        d_dict = dict(d.items())
        print(d_dict)
