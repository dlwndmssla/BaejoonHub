from collections import deque
chain = {k:deque([int(i) for i in str(input())]) for k in range(4)}
check = {0:[(2,1),(4,3),(6,5)],1:[(1,2),(4,3),(6,5)],2:[(6,5),(3,4),(1,2)],3:[(5,6),(3,4),(1,2)]}
for _ in range(int(input())):
    x,y = list(map(int,input().split()))
    x,d = x-1,[0, 0, 0, 0]
    d[x],conn = y,[chain[i][j] for i in [0,1,2,3] for j in [-2,2] ]
    for i,j in check[x]:
        if (d[j//2] != 0) and conn[i] != conn[j]: d[i//2] = -d[j//2]
    for a,(i,b) in zip(d,chain.items()):
        if a == 1:b.appendleft(b.pop())
        elif a == -1:b.append(b.popleft())
        chain[i] = b
print(sum((chain[i][0])*pow(2,i) for i in range(4)))
