a = int(input())

for i in range(1,a+a,2):
    for j in range((a+a-1-i)//2):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()

for i in range(a+a-3,0,-2):
    for j in range((a+a-1-i)//2):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()
