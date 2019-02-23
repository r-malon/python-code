while True:
    x = int(input("Digite quantos conteineres estão sendo carregados: "))
    while x < 50:
        y = 50 - x
        print('Ainda cabem %d' % y)
        x = int(input("Digite quantos conteineres a mais estão sendo carregados: "))
        if x == 50:
            print('No limite!!!')
            break
        elif x > 50:
            print("Pare!!!, foram %d conteineres a mais" % (x-50))
            break
