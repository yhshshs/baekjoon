while(True):
    a = int(input())
    if(a==-1):
        break
    arr = []
    for i in range(1,int(a**(1/2))+1):
        if(a%i == 0):
            arr.append(i)
            if(i**2 != a and a//i != a):
                arr.append(a//i)
    arr.sort()
    sum = 0

    for i in arr:
        sum+=i
    if(sum == a):
        print(a,"= ",end="")
        for i in range(len(arr)):
            if(i == 0):
                print(arr[i],end="")
            else:
                print(" +",arr[i],end="")
        print()
    else:
        print(a,"is NOT perfect.")