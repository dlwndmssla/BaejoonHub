import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
for i in range(n):
    ex = list(map(int,input().split()))
    graph.append(ex)

def bfs(graph):
    queue = deque()
    visited = [[False for i in range(m)]for j in range(n)]
    v = [0,0]    
    queue.append(v)
    while queue:
        v = queue.popleft()
        y,x = v
        visited[y][x] = True
        for t in range(4):
            x0 = x + [-1,1,0,0][t]
            y0 = y + [0,0,-1,1][t]
            if 0 <= x0 <= m-1 and 0 <= y0 <= n-1:
                if not visited[y0][x0] and graph[y][x] == 0:
                    if graph[y0][x0] == 0:
                        v0 = [y0, x0]
                        queue.append(v0)
                    elif graph[y0][x0] == 1 and graph[y][x] == 0:
                        graph[y0][x0] = 'c'
                    visited[y0][x0] = True
    cheese = sum([graph[i].count('c') for i in range(n)])                
    return cheese,graph

cheese0 = 0 
cnt = 0
while True:
    cnt += 1
    cheese, graph = bfs(graph)
    if cheese == 0: break
    cheese0 = cheese
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'c':
                graph[i][j] = 0

print(cnt-1)
print(cheese0)
