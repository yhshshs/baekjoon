n = int(input())
i = 1
while(True):
    if(n-i>0):
        n -= i
        i+=1
    else:
        break

if(i%2 == 0):
    print(str(n)+"/"+str(i+1-n))
else:
    print(str(i+1-n)+"/"+str(n))