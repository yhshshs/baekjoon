a, b = map(int,input().split())
arr = [i for i in range(1,a+1)]
for i in range(b):
    c , d = map(int,input().split())
    e = arr[c-1]
    arr[c-1] = arr[d-1]
    arr[d-1] = e

for i in arr:
    print(i,end=" ")