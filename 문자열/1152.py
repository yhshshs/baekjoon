a = input()
if(a[0]== " "): sum = 0
else: sum=1
for i in range(0,len(a)-1):
    if(a[i]==" "):
        sum+=1
print(sum)