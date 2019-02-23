p1 = input('telefonou a vitima? ')
p2 = input('local do crime? ')
p3 = input('mora perto? ')
p4 = input('trabalhava c/ a vitima? ')
p5 = input('devia a vitima? ')
x = [p1, p2, p3, p4, p5]
i = x.count('sim')
if i == 2:
    print('suspeito')
elif i == 3 or i == 4:
    print('cumplice!')
elif i > 4:
    print('assassino!')
else:
    print('inocente')
