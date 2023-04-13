a = int(input())
b = int(input())
arr = []

for i in range(a,b+1):
    brr = []
    for j in range(2,int(i**(1/2))+1):
        if(i%j==0):
            brr.append(i)
    if(len(brr)==0 and i!=1):
        arr.append(i)


if(len(arr)>0):
    print(sum(arr))
    print(min(arr))
else:
    print(-1)
