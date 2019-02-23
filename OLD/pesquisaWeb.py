import webbrowser as web
print('digite QUIT para encerrar...')
while True:
    x = input('digite o que vai pesquisar: ')
    if x.upper() == 'QUIT':
        break
    web.open('http://pt.wikipedia.org/wiki/%s' % x.title(), new=2)
