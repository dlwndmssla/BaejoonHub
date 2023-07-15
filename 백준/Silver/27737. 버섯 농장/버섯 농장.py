import sys
import math
from collections import deque
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline 

n,m,k = map(int,input().split())

graph = []

for i in range(n):
    ex = list(map(int,input().split()))
    for j in range(n):
        if ex[j] == 1:
            ex[j] = -1
    graph.append(ex)
    
def bfs(graph,x,y):
    queue = deque()
    v = [y,x]
    queue.append(v)
    while queue:
        v = queue.popleft()
        y,x = v
        for t in range(4):
            x0, y0 = x + [-1,1,0,0][t], y + [0,0,-1,1][t]
            if  0 <= x0 <= n-1 and 0 <= y0 <= n-1:
                if graph[y0][x0] == 0:
                    graph[y0][x0] = graph[y][x]
                    v0 = [y0,x0]
                    queue.append(v0)
                    
    return graph

cnt = 1
cnt_list = [0]
for y in range(n):
    for x in range(n):
        if graph[y][x] == 0:
            graph[y][x] = cnt
            graph = bfs(graph,x,y)
            sum0 = sum([graph[s].count(cnt) for s in range(n)])
            cnt_list.append(sum0)
            cnt += 1

for i in range(1,len(cnt_list)):
    a = math.ceil(cnt_list[i]/k)
    m -= a
    if m < 0:
        break

if sum([sum(graph[s]) for s in range(n)]) == -n*n:
    print('IMPOSSIBLE')
elif m >= 0:
    print('POSSIBLE')
    print(m)
else:    
    print('IMPOSSIBLE')