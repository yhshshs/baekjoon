a, b = map(int, input().split())
c = int(input())

d = a*60+b+c
if(d>=1440):
    d -= 1440
print(int(d/60),d%60)