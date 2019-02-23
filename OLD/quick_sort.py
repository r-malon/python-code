def quicksort(arr):
    x=[]
    for i in arr:
        if i > arr[0]:
            x.insert(len(x),i)
        else:
            x.insert(0,i)
    return x

print(quicksort([4,5,3,7,2]))
print(quicksort([3,8,98,23,12]))
