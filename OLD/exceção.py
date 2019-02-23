class Calculator():
    def power(self,n,p):
        try:
            if n<0 or p<0:
                raise ValueError
            return n**p
        except ValueError:
            return 'n and p should be non-negative'
