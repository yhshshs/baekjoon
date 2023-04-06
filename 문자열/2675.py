a = int(input())
for i in range(a):
    b,c = input().split()
    for z in c:
        for j in range(int(b)):
            print(z,end="")
    print()
