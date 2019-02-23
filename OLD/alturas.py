n = int(input('qnts: '))
l = []
for i in range(n):
    y = int(input('diga a altura: '))
    while y <= 0:
        y = int(input('diga a altura: '))
    else:
        l.append(y)
print('media é ', sum(l)/n)
print('menor é ', min(l))
print('maior é ', max(l))
