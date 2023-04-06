str1 = ""
N, B = map(int,input().split())
while(N//B!=0):
    if((N%B) in [0,1,2,3,4,5,6,7,8,9]):
        str1+=str(N%B)
    else : str1+=chr(55+N%B)
    N = N//B
if(N in [0,1,2,3,4,5,6,7,8,9]):
        str1+=str(N)
else : str1+=chr(55+N)
print(str1[::-1])
