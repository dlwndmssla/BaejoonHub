from collections import deque
chain = {k:deque([int(i) for i in str(input())]) for k in range(4)}
check = {0:[(2,1),(4,3),(6,5)],
1:[(1,2),(4,3),(6,5)],
2:[(6,5),(3,4),(1,2)],
3:[(5,6),(3,4),(1,2)]}

for _ in range(int(input())):
    x,y = list(map(int,input().split()))
    x = x-1
    conn = [chain[i][j] for i in [0,1,2,3] for j in [-2,2] ]
    d = [0, 0, 0, 0]
    d[x] = y
    # print(conn)
    for i,j in check[x]:
        # print(i//2,j//2)
        if (d[j//2] != 0) and conn[i] != conn[j]:
            d[i//2] = -d[j//2]
    # print("d",d)

    for i,b in chain.items():
        a = d[i]
        if a == 1:
            c = b.pop()
            b.appendleft(c)
        elif a == -1:
            c = b.popleft()
            b.append(c)
        chain[i] = b
        # print(chain[i])

print(sum((chain[i][0])*pow(2,i) for i in range(4)))


