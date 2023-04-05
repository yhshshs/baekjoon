board = []
eq = 0
b = 0
w = 0
M,N = map(int,input().split())
for i in range(M):
    inBoard = input()
    board.append(inBoard)

for i in range(M-7):
    for j in range(N-7):

        for z in range(8):
            for x in (board[z+i][j:j+8]):
                if(eq == 0 and x =="B"):
                    b +=1
                    eq = 1
                if(eq ==1 and x=="W"):
                    w +=1
                    eq = 0
            if(eq ==0): eq = 1
            else : eq = 0
        print(b,w)
        b = 0
        w = 0



