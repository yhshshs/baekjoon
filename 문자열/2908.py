a = input()
rea =""
for i in range(len(a)-1,-1,-1):
    rea+=a[i]
b,c = map(int,rea.split())
if(b>c):
    print(b)
else:
    print(c)

# print(max(input()[::-1].split()))