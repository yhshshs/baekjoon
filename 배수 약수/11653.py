a = int(input())
arr = []
while(a!=1):
    for i in range(2,a+1):
        if(a%i==0):
            a=a//i
            arr.append(i)
            break

for i in arr:
    print(i)