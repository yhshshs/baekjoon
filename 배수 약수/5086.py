# while (True):
#     a, b = map(int, input().split())
#     if(a==0 and b==0):
#         break

#     arr = []
#     brr = []
#     for i in range(1, a//2+1):
#         if (a % i == 0):
#             if(i>a//i):
#                 if(i==a//i):
#                     brr.append(i)
#                 break
#             else:
#                 arr.append(i)
#                 arr.append(a//i)

#     for i in range(1, b//2+1):
#         if (b % i == 0):
#             if(i>=b//i):
#                 if(i==b//i):
#                     brr.append(i)
#                 break
#             else:
#                 brr.append(i)
#                 brr.append(b//i)            

#     if(a in brr):
#         print("factor")
#     elif(b in arr):
#         print("multiple")
#     else:
#         print("neither")

while(True):
    a,b = map(int,input().split())
    if(a ==0 and b==0):
        break

    if(a<b):
        n = b
        m = a
    else:
        n = a
        m = b

    