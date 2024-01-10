from collections import deque

def bfs(graph,x,y,visited):
    v = [y,x]
    queue = deque([v])
    visited[y][x] = True
    while queue:
        v = queue.popleft()
        y,x = v
        for k in range(4):
            x0,y0 = x+[0,0,-1,1][k],y+[-1,1,0,0][k]
            if not (0<= x0 <= m-1): continue 
            if not (0<= y0 <= n-1): continue
            if graph[y0][x0] == '#' and not visited[y0][x0]:
                queue.append([y0,x0])
                visited[y0][x0] = True
            
    return graph,visited
    
a = int(input())    
for _ in range(a):
    ans = 0
    n,m = map(int,input().split())
    graph = []
    visited = [[False for i in range(m)] for j in range(n)]
    for i in range(n):
        ex = str(input())
        graph.append(ex)
        
    for x in range(m):
        for y in range(n):
            if graph[y][x] == '#' and not (visited[y][x]):
                graph,visited = bfs(graph,x,y,visited)
                ans += 1
    
    print(ans)      
    