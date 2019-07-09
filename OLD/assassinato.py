p1 = input('Telefonou a vitima? ')
p2 = input('Local do crime? ')
p3 = input('Mora perto? ')
p4 = input('Trabalhava c/ a vitima? ')
p5 = input('Devia a vitima? ')
x = [p1, p2, p3, p4, p5]
i = x.count('sim')
if i == 2:
    print('Suspeito')
elif i == 3 or i == 4:
    print('Cúmplice!')
elif i > 4:
    print('Assassino!')
else:
    print('Inocente')
