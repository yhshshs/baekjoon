a,b = map(int,input().split())
arr = list(map(int,input().split()))
astr = ""
for i in arr:
    if(i<b):
        astr+=str(i)+" "

print(astr)
