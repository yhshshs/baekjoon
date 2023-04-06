n = input()
arr = list(map(int,input().split()))
findn = int(input())
sum = 0
for i in arr:
    if(i==findn):
        sum+=1
print(sum)

print(arr.count(findn))