import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def bfs(graph,v_list):
    queue = deque(v_list)
    visited = [[1000 for i in range(m)] for j in range(n)]
    while queue:
        v = queue.popleft()
        y,x = v
        if v in v_list:
            visited[y][x] = 0
        for k in range(8):
            x0,y0 = x+[1,1,1,0,0,-1,-1,-1][k],y+[1,0,-1,1,-1,1,0,-1][k]
            if not (0<= x0 <= m-1): continue 
            if not (0<= y0 <= n-1): continue
            if graph[y0][x0] == 0 and (visited[y0][x0] > visited[y][x]+1):
                queue.append([y0,x0])
                visited[y0][x0] = visited[y][x]+1
                        
    return visited

n,m = map(int,input().split())

graph = []
v_list = []
for i in range(n):
    ex = list(map(int,input().split()))
    graph.append(ex)
    if 1 in ex:
        for j in range(m):
            if ex[j]==1:
                v_list.append([i,j])
  
visited = bfs(graph,v_list)              
ans = max([max(visited[i]) for i in range(len(visited))])
print(ans)