N,M = map(int,input().split())
arr1 = [i for i in range(1,N+1)]
for i in range(M):
    a,b,c = map(int,input().split())
    arr1 = arr1[:a-1]+arr1[c-1:b]+arr1[a-1:c-1]+arr1[b:]

for i in arr1:
    print(i,end=" ")