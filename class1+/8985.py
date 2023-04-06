n = int(input())
for i in range(n):
    res = 0
    score = 1
    str = input()
    for j in str:
        if(j=="O"):
            res+=score
            score+=1
        else:
            score = 1
    print(res)