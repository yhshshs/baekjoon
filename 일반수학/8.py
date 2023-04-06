N, B = input().split()
B=int(B)
sum = 0
for i in range(len(N)-1,-1,-1):
    if(N[i] in ["0","1","2","3","4","5","6","7","8","9"]):
        sum += int(N[i])*(B**(len(N)-i-1))

    else: sum += (ord(N[i])-55)*(B**(len(N)-i-1))
print(sum)

n,b=input().split()
print(int(n,int(b)))