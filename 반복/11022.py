import sys
a = int(input())
arr1 = []

for i in range(a):
    b,c = map(int,sys.stdin.readline().split())
    arr1.append("Case #"+str(i+1)+": "+str(b)+" + "+str(c)+" = "+str(b+c))

print
for i in arr1:
    print(i)