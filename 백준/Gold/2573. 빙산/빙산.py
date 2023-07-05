import sys
import copy
from collections import deque
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

n,m = map(int, input().split())
graph = []

for i in range(n):
    ex = list(map(int, input().split()))
    graph.append(ex)

def bfs(graph,x,y,ice,visited):
    queue = deque()
    queue.append([y,x])
    while queue:
        v = queue.popleft()
        y,x = v
        if not visited[y][x] and ice[y][x] > 0:    
            cnt = [ice[y-1][x],ice[y+1][x],ice[y][x-1],ice[y][x+1]].count(0)
            graph[y][x] = max(0,ice[y][x]-cnt)
            visited[y][x] = True  
        for t in range(4):
            y0,x0 = y + [0,0,-1,1][t], x + [-1,1,0,0][t]   
            if 0 <= x0 <= m-1 and 0 <= y0 <= n-1:
                if ice[y0][x0] > 0 and ice[y0][x0] == graph[y0][x0] and not visited[y0][x0]:
                    cnt = [ice[y0-1][x0],ice[y0+1][x0],ice[y0][x0-1],ice[y0][x0+1]].count(0)
                    graph[y0][x0] = max(0,ice[y0][x0]-cnt)
                    queue.append([y0,x0])
                    visited[y0][x0] = True     
    
    return graph,visited

year = 0
if sum([sum(graph[i]) for i in range(n)]) == 0:
    print(0)
else:
    while True:
        ice = copy.deepcopy(graph)
        count0 = 0
        visited = [[False for i in range(m)] for j in range(n) ]
        for x in range(m):
            for y in range(n):
                if graph[y][x] > 0 and graph[y][x] == ice[y][x] and not visited[y][x]:
                    graph,visited = bfs(graph,x,y,ice,visited)
                    count0 += 1

        year += 1
        if count0 >= 2: 
            print(year-1)
            break
        elif sum([sum(graph[i]) for i in range(n)]) == 0:
            print(0)
            break 