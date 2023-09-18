moves = [[4,6], [6,8], [7,9], [4,8], [0,3,9], [], [0,1,7], [2,6], [1,3], [2,4]]

lenmoves = [*map(len, moves)]

def moves_from_k(k,n):
    if n ==1:
        return lenmoves[k]
    return sum(moves_from_k(j, n-1) for j in moves[k])

for i in range(1,30):
    print(i, sum(moves_from_k(j, i) for j in range(10)))
