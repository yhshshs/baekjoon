arr = []
while(True):
    a,b = map(int,input().split())
    if(a==0 and b==0):
        break
    arr.append(a+b)
for i in arr:
    print(i)