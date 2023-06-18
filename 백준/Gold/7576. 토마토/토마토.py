#7576
import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

m,n = map(int, input().split())
graph = []

for i in range(n):
    ex = list(map(int, input().split()))
    graph.append(ex)

def bfs(graph,x,y, vlist):
    queue = deque(vlist)
    while queue:
        v = queue.popleft()
        y,x = v[0], v[1]
        for t in range(4):
            x0 = x + [-1,1,0,0][t]
            y0 = y + [0,0,-1,1][t]
            if 0 <= x0 <= m-1 and 0 <= y0 <= n-1:
                if graph[y0][x0] == 0:
                    queue.append([y0,x0])
                    graph[y0][x0] = graph[y][x] + 1


vlist = []
for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:
            vlist.append([y,x])

bfs(graph, x,y, vlist)

for s in range(n):
    if 0 in graph[s]:
        print(-1)
        break
    if s == n-1:
        print(max([max(graph[s]) for s in range(n)])-1)
