arr = []
max = 0
num = 0
for i in range(9):
    arr.append(int(input()))
    if(max<arr[i]):
        max=arr[i]
        num = i+1

print(max)
print(num)