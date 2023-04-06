a = input()
sum=0
for i in a:
    if(i in ["P","Q","R","S"]):
        sum+=7
    elif(i in ["T","U","V"]):
        sum+=8
    elif(i in ["W","X","Y","Z"]):
        sum+=9
    else:
        sum+=(ord(i)-59)//3
    sum+=1
print(sum)