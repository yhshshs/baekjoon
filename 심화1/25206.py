sumScore=0
sumGrade=0
pnum=0
grade = ["A+","A0","B+","B0","C+","C0","D+","D0"]

for i in range(20):
    a,b,c = input().split()

    if(c=="P"):
        pnum+=1
        continue

    sumScore+=float(b)

    if(c!="F"):
        sumGrade += float(b)*(4.5-grade.index(c)*0.5)


print(sumGrade/sumScore)