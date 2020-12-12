d = {}

m_s = input('ведите строку: ')

for symbol in m_s:
    keys = d.keys()
    if symbol in keys:
        d[symbol] += 1
    else:
        d[symbol] = 1
print(d)