a = input().lower()
many = []
aind = []

for i in a:
    if(i in aind):
        many[aind.index(i)]+=1
    else:
        aind.append(i)
        many.append(1)

n=0
mm = max(many)
for i in many:
    if(i==mm):
        n+=1

if(n>1):
    print("?")
else:
    res = aind[many.index(mm)]
    print(res.upper())