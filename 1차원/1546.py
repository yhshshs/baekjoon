a = int(input())
sum = 0
arr = list(map(int,input().split()))
arr.sort()
for i in arr:
    sum += i
print(sum/arr[-1]/a*100)