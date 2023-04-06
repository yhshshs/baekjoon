a, b = map(int, input().split())
c = a*60+b-45
if(c<0):
    c += 1440
print(int(c/60),c%60)