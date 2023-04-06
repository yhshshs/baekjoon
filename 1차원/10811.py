a,b = map(int,input().split())
arr = [i for i in range(1,a+1)]

for i in range(b):
    c,d = map(int,input().split())
    c -= 1
    d -= 1

    if((d-c)%2 == 0):
        num = (d-c)//2
    else:
        num = (d-c)//2+1

    for j in range(num):
        e = arr[c+j]
        arr[c+j] = arr[d-j]
        arr[d-j] = e
for i in arr:
    print(i,end=" ")
