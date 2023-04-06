a = int(input())
arr = []
for i in range(a):
    b,c = map(int,input().split())
    arr.append(b+c)
for i in arr:
    print(i)