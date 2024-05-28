symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
symbolist = symbols.split(',')
print(symbolist)

print(symbolist[0])
print(symbolist[1])
print(symbolist[-1])
print(symbolist[-2])

symbolist[2] = 'AIG'
print(symbolist)

mysyms = []
mysyms.append('GOOG')
print(mysyms)

symbolist[-2:] = mysyms
print(symbolist)

for i in symbolist:
    print(f's={i}')

print('AIG' in symbolist)

symbolist.insert(1, 'AA')
print(symbolist)

symbolist.append('YHOO')
print(symbolist)

print(symbolist.count('YHOO'))

print(symbolist.index('YHOO'))

symbolist.remove('YHOO')
print(symbolist)



