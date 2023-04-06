a = int(input())
n = 0

for i in range(1,a+1):
    n = 0
    for j in range(1,a+1):
        if(a-i <= n):
            print("*",end="")
        else:
            print(" ",end="")
        n+=1
    print()