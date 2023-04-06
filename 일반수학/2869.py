u,d,h = map(int,input().split())
i = 1

hmu = h-u
ud = u-d
day=h-(hmu//ud)*ud

while(True):
    if(day-u<=0):
        break
    else:
        day = day - u + d
        i+=1
print(i+hmu//ud)


# 15 9 55
# 40 6 6
# 55 - 36
# 19
# 15 6 21 12 27 18 33 24 39 30 45 36 51 42 57