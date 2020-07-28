n = int(input('Quantia de alturas: '))
l = []

for i in range(n):
    y = int(input('Diga a altura: '))
    while y <= 0:
        y = int(input('Diga a altura: '))
    else:
        l.append(y)

print('media é ', sum(l)/n)
print('menor é ', min(l))
print('maior é ', max(l))