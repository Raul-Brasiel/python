def insertion_sort(v):
    n = len(v)
    for i in range(1,n):
        x = v[i]
        j = i - 1
        while j >= 0 and v[j] > x:
            v[j + 1] = v[j]
            j-= 1
        v[j+1] = x
v = [5,1,2,4,3]
print(v)
insertion_sort(v)
print(v)