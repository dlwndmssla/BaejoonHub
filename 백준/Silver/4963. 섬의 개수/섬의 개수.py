import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(graph,x,y,visited):
    visited[y][x] = True
    for t in range(8):
        x0 = [0,0,-1,1,-1,-1,1,1][t] + x
        y0 = [-1,1,0,0,-1,1,-1,1][t] + y
        if 0<=y0<=n-1 and 0<=x0<=m-1 and graph[y0][x0] == 1: 
            if not visited[y0][x0]:
                visited[y0][x0] = True
                dfs(graph,x0,y0,visited)
            
while True:
    ex = list(map(int, input().split()))
    if ex == [0,0]:
        break
    else:
        m,n = ex[0],ex[1]
    visited = [[False for q in range(m)] for w in range(n)]
    graph = [[0 for q in range(m)] for w in range(n)]
    for r in range(n):
        ex1 = list(map(int, input().split()))
        graph[r] = ex1
        
    c = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visited[i][j] == False:
                x,y = j,i
                dfs(graph,x,y,visited)
                c += 1
                
    print(c)