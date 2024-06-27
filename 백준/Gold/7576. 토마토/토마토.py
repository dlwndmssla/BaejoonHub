#미로탐색
import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

m,n = list(map(int,input().split()))

graph = [] 
v_list = []
for i in range(n):
    ex = list(map(int,input().split()))
    for j in range(m):
        if ex[j] == 1:
            v_list.append([i,j])
    graph.append(ex) 


def bfs(v_list):
    queue = deque(v_list)
    while queue:
        y,x = queue.popleft()
        cnt = graph[y][x]+1
        for t in range(4):
            y0,x0 = y+[0,0,-1,1][t],x+[-1,1,0,0][t]
            if not ((0<= y0 <=n-1) and (0<= x0<=m-1)) : continue
            if graph[y0][x0] == -1: continue
            if 0 < graph[y0][x0] <= cnt: continue
            graph[y0][x0] = cnt
            queue.append([y0,x0])
            

bfs(v_list)

con = False
max0 = 0
for i in range(n):
    for j in range(m):
        max0 = max(max0,graph[i][j])
        if graph[i][j] == 0:
            con = True
            break
        
if con: print(-1)
else: print(max0-1)
