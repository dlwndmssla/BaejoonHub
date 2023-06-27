#16234

import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

n,l,r = map(int,input().split())
graph = []
for i in range(n):
    ex = list(map(int,input().split()))
    graph.append(ex)
def bfs(graph,x,y,visited):
    queue = deque()
    v = [y,x]
    queue.append(v)
    visited[y][x] = True
    people = graph[y][x]
    kd = 1
    list0 = [v]
    while queue:
        y,x = queue.popleft()
        for t in range(4):
            x0 = x + [-1,1,0,0][t]
            y0 = y + [0,0,-1,1][t]
            if 0 <= x0 <=n-1 and 0 <= y0 <=n-1:
                if l<=  abs(graph[y][x] - graph[y0][x0] ) <= r and not visited[y0][x0]:
                    people += graph[y0][x0]
                    kd += 1
                    v0 = [y0,x0]
                    queue.append(v0)
                    list0.append(v0)
                    visited[y0][x0] = True
                    
    return visited,people,kd,list0

for s in range(2000):
    visited = [[ False for i in range(n)] for i in range(n)]
    vlist = []
    for y in range(n):
        for x in range(n):          
            if not visited[y][x]:
                
                visited,people0,kd0,list0 =  bfs(graph,x,y,visited)
                if kd0 != 1:
                    kd0 = int(people0/kd0)
                    vlist.append(kd0)
                    vlist.append(list0)

    if len(vlist) != 0:
        for i in range(0,len(vlist),2):
            for j in vlist[i+1]:
                a,b = j
                graph[a][b] = vlist[i]
    else: 
        print(s)
        break