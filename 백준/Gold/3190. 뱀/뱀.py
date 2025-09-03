from collections import deque

n,k = int(input()),int(input())
grid = {tuple(map(int,input().split())):1 for i in range(k)}
l = int(input())
chg = list(list(map(str,input().split())) for i in range(l))
chg.append((int(chg[-1][0])+100,chg[-1][1]))

dir = [(0,1),(1,0),(0,-1),(-1,0)]
d,t,y,x = 0,0,1,1
dummy = deque([(y,x)])

for i,j in chg:
    dy,dx = dir[d]
    while t < int(i):
        t += 1
        y,x = y+dy,x+dx
        if (y,x) in dummy: print(t); exit()
        if not (1<=y<=n and 1<=x<=n): print(t); exit()
        dummy.append((y,x))
        if not grid.get((y,x),0): dummy.popleft(); continue 
        grid[(y,x)] = 0            

    if j == 'D': d = (d+1)%4
    if j == 'L': d = (d-1)%4

