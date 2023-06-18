import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

m,n,h = map(int, input().split())

graph = []
for i in range(h):
    ex1 = []
    for j in range(n):
        ex = list(map(int, input().split()))
        ex1.append(ex)
    graph.append(ex1)

# z,y,x순서
vlist = []

for i in range(h): #z
    for j in range(n): #y
        for k in range(m): #x
            if graph[i][j][k] == 1:
                vlist.append([i,j,k])

def bfs(graph,vlist):
    queue = deque(vlist)
    while queue:
        v = queue.popleft()
        z,y,x = v[0],v[1],v[2]
        for t in range(6):
            x0 = x +[-1,1,0,0,0,0][t]
            y0 = y +[0,0,-1,1,0,0][t]
            z0 = z +[0,0,0,0,-1,1][t]
            if 0<= x0 <= m-1 and 0<= y0 <= n-1 and 0<= z0 <= h-1:
                if graph[z0][y0][x0] == 0:
                    graph[z0][y0][x0] = graph[z][y][x] + 1
                    node0 = [z0,y0,x0]
                    queue.append(node0)

bfs(graph,vlist)            

max0 = 0
check = False
for i in range(h): #z
    for j in range(n): #y
        for k in range(m): #x
            if graph[i][j][k] == 0:
                max0 = 0
                check = True
                break
            elif max0 < graph[i][j][k]:
                max0 = graph[i][j][k]
                
        if check: break
    if check: break

print(max0-1)   