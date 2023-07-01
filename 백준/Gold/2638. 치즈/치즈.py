import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def bfs(graph):
    visited = [[False for i in range(m)] for i in range(n)]
    v = [0,0]
    queue = deque()
    queue.append(v)
    graph[0][0] = 'a'
    while queue:
        v = queue.popleft()
        y,x = v
        visited[y][x] = True
        for t in range(4):
            x0 = x + [-1,1,0,0][t]
            y0 = y + [0,0,-1,1][t]
            if 0 <= x0 <= m-1 and 0 <= y0 <= n-1:
                if not visited[y0][x0]:
                    if graph[y0][x0] == 0:
                        graph[y0][x0] = 'a'
                        visited[y0][x0] = True
                        v0 = [y0,x0]
                        queue.append(v0)

    v = [0,0]
    queue = deque()
    queue.append(v)
    visited = [[False for i in range(m)] for i in range(n)]
    while queue:
        v = queue.popleft()
        y,x = v
        visited[y][x] = True
        for t in range(4):
            x0 = x + [-1,1,0,0][t]
            y0 = y + [0,0,-1,1][t]
            if 0 <= x0 <= m-1 and 0 <= y0 <= n-1:
                if graph[y0][x0] == 1 and graph[y][x] == 'a' and not visited[y0][x0]:
                    if [graph[y0-1][x0],graph[y0+1][x0],graph[y0][x0-1],graph[y0][x0+1]].count('a') >= 2:
                        graph[y0][x0] = 'c'
                        v0 = [y0,x0]
                        queue.append(v0)
                        visited[y0][x0] = True
                elif graph[y0][x0] == 'a' and graph[y][x] == 'a' and not visited[y0][x0]:
                    v0 = [y0,x0]
                    queue.append(v0)
                    visited[y0][x0] = True

    cheese = sum([graph[i].count('c') for i in range(n)])                
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'a' or graph[i][j] == 'c': 
                graph[i][j] = 0
            
    return cheese,graph

n,m = map(int,input().split())
graph = []
for i in range(n):
    ex = list(map(int,input().split()))
    graph.append(ex)

cnt = 0
while True:
    cnt += 1
    cheese, graph = bfs(graph)
    if cheese == 0: break

print(cnt-1)   
    