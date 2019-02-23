def ola(n):
        for i in range(n, 0, -1):
                if i%2==0:
                        print('*-'*i)
                else:
                        print('*-'*(i-1)+'*')

ola(5)
