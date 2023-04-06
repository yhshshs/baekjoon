n = int(input())
for i in range(n):
    price = int(input())
    q = price//25
    price -= q*25
    diam = price//10
    price -= diam*10
    nic = price//5
    price -= nic*5
    print(q,diam,nic,price)