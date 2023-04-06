a = int(input())
arr1 = []

for i in range(a):
    b,c = map(int,input().split())
    arr1.append(b+c)

for i in range(len(arr1)):
    print("Case #"+str(i+1)+":",arr1[i])