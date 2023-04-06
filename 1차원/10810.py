a,b = map(int,input().split())
arr = [0 for i in range(a)]
for i in range(b):
    a1,b1,c1 = map(int,input().split())
    for j in range(b1-a1+1):
        arr[a1+j-1] = c1
for i in arr:
    print(i,end=" ")