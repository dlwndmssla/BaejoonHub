import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def bfs(graph,jihoon,fire):
    queue = deque(fire)
    while queue:
        v = queue.popleft()
        y,x = v
        if graph[y][x] == 'F':
            graph[y][x] = 0
        for t in range(4): 
            x0 = x + [-1,1,0,0][t]
            y0 = y + [0,0,-1,1][t]
            if 0 <= x0 <= m-1 and 0 <= y0 <= n-1:
                if graph[y0][x0] == '.' or graph[y][x] == 'J':
                    graph[y0][x0] = graph[y][x] - 1
                    v0 = [y0,x0]
                    queue.append(v0)

    queue = deque(jihoon)
    y,x = jihoon[0]
    graph[y][x] = 'J'
    while queue:
        v = queue.popleft()
        y,x = v
        if graph[y][x] == 'J':
            graph[y][x] = 0
        for t in range(4): 
            x0 = x + [-1,1,0,0][t]
            y0 = y + [0,0,-1,1][t]
            if 0 <= x0 <= m-1 and 0 <= y0 <= n-1:
                if type(graph[y0][x0]) == int:                   
                    if graph[y0][x0] <= 0 and abs(graph[y][x])+1 < abs(graph[y0][x0]):
                        graph[y0][x0] = graph[y][x] + 1
                        v0 = [y0,x0]
                        queue.append(v0)       
                elif graph[y0][x0] == '.':
                    graph[y0][x0] = graph[y][x] + 1
                    v0 = [y0,x0]
                    queue.append(v0)
                    
    return graph

n,m = map(int,input().split())

graph = []
jihoon = []
fire = []

for i in range(n):
    ex = list(map(str,input().strip()))
    for j in range(m):
        if ex[j] == 'J':
            jihoon.append([i,j])
        elif ex[j] == 'F':
            fire.append([i,j])           
    graph.append(ex)
        
graph = bfs(graph,jihoon,fire)

min0 = []
for i in range(n):
    for j in range(m):
        if i in [0,n-1] or j in [0,m-1]:
            if type(graph[i][j]) == int and [i,j] not in fire:
                if graph[i][j] >= 0:
                    min0.append(graph[i][j])

if len(min0) == 0:
    print('IMPOSSIBLE')
else:
    print(min(min0)+1)