res=[[0 for i in range(100)] for i in range(100)]
sum = 0
n = int(input())
for i in range(n):
    w,h = map(int,input().split())
    for j in range(w,10+w):
        for z in range(h,10+h):
            res[j][z]="1"

for i in res:
    sum +=i.count("1")
print(sum)
