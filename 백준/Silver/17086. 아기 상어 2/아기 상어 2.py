#미로탐색
import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

n,m = list(map(int,input().split()))
 
graph = []
shark = []
for i in range(n):
    ex = list(map(int,input().split()))
    graph.append(ex)
    for j in range(m):
        if ex[j] == 1:
            shark.append([i,j])

def bfs(shark):
    queue = deque(shark)
    while queue:
        y,x = queue.popleft()
        cnt = graph[y][x]
        for t in range(8):
            y0,x0 = y+[-1,-1,-1,0,0,1,1,1][t],x+[-1,0,1,-1,1,-1,0,1][t]
            if not ((0<= y0 <=n-1) and (0<= x0<=m-1)) : continue
            if graph[y0][x0] != 0: continue
            graph[y0][x0] = cnt+1
            queue.append([y0,x0])
    
    return graph
    
ans = bfs(shark)

print(max([max(ans[i]) for i in range(n)])-1)
