a = int(input())
sum = 0
avg = 0
over = 0
for i in range(a):
    li = list(map(int,input().split()))
    for j in range(1,len(li)):
        sum+=li[j]
    avg = sum//li[0]
    for z in range(1,len(li)):
        if(li[z]>avg):
            over +=1
    print(format(over/li[0]*100,".3f"),end="")
    print("%")
    sum = 0
    avg = 0
    over = 0