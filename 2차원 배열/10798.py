result = [[] for i in range(15)]
for i in range(5):
    str1 = input()
    for j in range(len(str1)):
        result[j].append(str1[j])

for i in result:
    for j in i:
        print(j,end="")

