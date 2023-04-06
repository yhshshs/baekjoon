a=input()
pel = 0
for i in range(len(a)//2):
    if(a[i]!=a[-i-1]):
        pel = 1

if(pel==1):
    print(0)
else:
    print(1)