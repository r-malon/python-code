def wrap(string, max_width):
    txt=''
    for i in range(len(string)):
        if i%max_width==0:
            txt+=string[i:i+max_width]+'\n'
    return txt
x=wrap('abcdefghij', 6)
print(x)
