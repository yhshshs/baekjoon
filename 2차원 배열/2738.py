N,M = map(int,input().split())
arr=[]
for i in range(N):
    a = list(map(int,input().split()))
    arr.append(a)

for i in range(N):
    a = list(map(int,input().split()))
    for j in range(len(a)):
        arr[i][j]+=a[j]

for i in arr:
    for j in i:
        print(j,end=" ")
    print()