import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

n,k = map(int,input().split())
graph = []
virus = []

for i in range(n):
    ex = list(map(int,input().split()))
    for j in range(n):
        if ex[j] != 0:
            virus.append([i,j,ex[j]])
            ex[j] = 10000*ex[j]
    graph.append(ex)
virus.sort(key=lambda x : (x[2]))

s,a,b = map(int,input().split())

def bfs(graph,virus):
    queue = deque(virus)
    while queue:
        v = queue.popleft()
        y,x = v[0],v[1]
        for t in range(4):
            x0 = x + [-1,1,0,0][t]
            y0 = y + [0,0,-1,1][t]
            if 0 <= x0 <= n-1 and 0 <= y0 <= n-1:
                if graph[y0][x0] == 0:
                    graph[y0][x0] = graph[y][x] + 1
                    v0 = [y0, x0]
                    queue.append(v0)

bfs(graph,virus)
ans = int(graph[a-1][b-1])
if ans%10000 <= s:
    print(int(ans/10000))
else:
    print(0)
