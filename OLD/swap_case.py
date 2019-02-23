def swap_case(s):
    text = ''
    for x in s:
        if x.isupper():
            text += x.lower()
        else:
            text += x.upper()
    return text

s = input('Digite: ')
result = swap_case(s)
print(result)
