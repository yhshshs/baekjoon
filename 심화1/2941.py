cro = ["c=","c-","dz=","d-","lj","nj","s=","z="]
a = input()

alen = len(a)
n = 0
n1=0

for i in cro:
    if(i in a):
        a=a.replace(i,"!")
        n += (alen - len(a)+1)//len(i)
        alen=len(a)

print(len(a))