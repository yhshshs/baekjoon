n1 = int(input())
word = ""
sum = 0
for i in range(n1):
    str1 = list(input())
    word=""
    for j in range(len(str1)):
        if(str1[j]==word):
            str1[j]=j
        else:
            word = str1[j]
    for j in range(len(str1)):
        if(str1[j] in str1[j+1:]):
            sum+=1
            break
print(n1-sum)
