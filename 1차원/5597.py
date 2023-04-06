arr = [i for i in range(1,31)]
for i in range(28):
    a = int(input())
    arr.remove(a)
for i in arr:
    print(i,end=" ")