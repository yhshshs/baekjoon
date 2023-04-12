while(True):
    a,b = map(int,input().split())

    if(a == 0 and b == 0):
        break

    c = max(a,b)
    arr =[]
    for i in range(1,c+1):
        if(c%i==0):
            arr.append(i)


    if(a>b and b in arr):
        print("multiple")
    elif(a<b and a in arr):
        print("factor")
    else:
        print("neither")