swaps=[(0,1),(0,3),(1,2),(1,4),(2,5),(3,4),(3,6),(4,5),(4,7),(5,8),(6,7),(7,8)]
primes=[3,5,7,11,13,17]

all=[(1,2,3,4,5,6,7,8,9)]
move={(1,2,3,4,5,6,7,8,9):0}
for board in all:
    for j in swaps:
        if board[j[0]]+board[j[1]] in primes:
            newboard=list(board)
            newboard[j[0]],newboard[j[1]]=newboard[j[1]],newboard[j[0]]
            newboard=tuple(newboard)
            if newboard not in move:
                all.append(newboard)
                move[newboard]=move[board]+1

for _ in range(int(input())):
    input()
    board=[]
    for i in range(3):
        board+=list(map(int,input().split()))
    board=tuple(board)
    if board in move:
        print(move[board])
    else:
        print(-1)