n=0
m=0
amax = 0
for i in range(9):
    arr = list(map(int,input().split()))
    sarr = list(arr)
    arr.sort(reverse=True)
    if(arr[0]>amax):
        amax = arr[0]
        n=i
        m=sarr.index(arr[0])

print(amax,n+1,m+1)
