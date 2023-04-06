n = int(input())-1
i = 0
while(True):
    if(n-i*6>0):
        n-=i*6
        i+=1
    else:
        break
print(i+1)