sum = 1
for i in range(3):
    a = int(input())
    sum *= a

res = [0 for i in range(10)]
for i in str(sum):
    res[int(i)]+=1
for i in res:
    print(i)