import sys

a = int(input())
arr1 = []

for i in range(a):
    b,c = map(int,sys.stdin.readline().split())
    arr1.append(b+c)

for i in range(len(arr1)):
    print(arr1[i])