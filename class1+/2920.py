arr1 = list(map(int,input().split()))
result = ""
if(arr1[0]==1):
    result = "ascending"
    for i in range(0,len(arr1)-1):
        if(arr1[i]+1!=arr1[i+1]):
            result = "mixed"
            break
elif(arr1[0]==8):
    result = "descending"
    for i in range(0,len(arr1)-1):
        if(arr1[i]-1!=arr1[i+1]):
            result = "mixed"
            break
else:
    result = "mixed"
        
print(result)