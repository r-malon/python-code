prev1 = 1
prev2 = 1
for i in range(300):
    print('%d - %d' % (i, prev1))
    print('%d - %d' % (i+1, prev2))
    prev1 = prev1 + prev2
    prev2 = prev1 + prev2
