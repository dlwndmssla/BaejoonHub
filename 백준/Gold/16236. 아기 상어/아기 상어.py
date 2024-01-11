import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def bfs(graph,v,shark):
    y,x = v
    queue = deque([v])
    visited = [[500 for i in range(n)] for j in range(n)]
    visited[y][x] = 0
    fish = []
    while queue:
        v = queue.popleft()
        y,x = v
        for k in range(4):
            x0,y0 = x+[0,0,-1,1][k],y+[-1,1,0,0][k]
            if not (0<= x0 <= n-1): continue 
            if not (0<= y0 <= n-1): continue
            if graph[y0][x0] <= shark and (visited[y0][x0] > visited[y][x]+1):
                queue.append([y0,x0])
                visited[y0][x0] = visited[y][x]+1
                if graph[y0][x0] < shark and graph[y0][x0] !=0:
                    fish.append([visited[y0][x0],y0,x0])
            
    return fish

n = int(input())
graph = []
for i in range(n):
    ex = list(map(int,input().split()))
    graph.append(ex)
    if 9 in ex:
        v = [i,ex.index(9)]

shark = 2
ss = 0
ans = 0

while True:
    fish = bfs(graph,v,shark)
    fish = sorted(fish, key= lambda x: (x[0],x[1],x[2]))

    if len(fish) == 0:
        break
    y,x = v
    graph[y][x] = 0
    ans += fish[0][0]
    v = fish[0][1:]
    ss += 1
    if ss == shark:
        shark += 1
        ss = 0
        
    graph[v[0]][v[1]] = shark
        
print(ans)