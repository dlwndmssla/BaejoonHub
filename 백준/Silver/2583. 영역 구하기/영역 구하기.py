import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# m= 가로, n= 세로 
m,n,k = map(int, input().split())
graph = [[1 for i in range(n)] for j in range(m)]
visited = [[False for i in range(n)] for j in range(m)]

for i in range(k):
    ex= list(map(int, input().split()))
    for x2 in range(ex[0],ex[2]):
        for y2 in range(ex[1],ex[3]):
            graph[y2][x2] = 0

def dfs(graph,x,y,visited):
    visited[y][x] = True
    for t in range(4):
        x0 = [-1,1,0,0][t] + x
        y0 = [0,0,-1,1][t] + y
        if 0 <= x0 <= n-1  and 0 <= y0 <= m-1 and graph[y0][x0] == 1:
            if not visited[y0][x0]:
                visited[y0][x0] = True
                dfs(graph, x0, y0, visited)
      
group = []          
c0 = 0
for q in range(n):
    for w in range(m):
        x,y = q,w
        if graph[y][x] == 1 and visited[y][x] == False:
            dfs(graph,x,y,visited)
            c1 = sum([sum(visited[e]) for e in range(m)])
            group.append(c1-c0)
            c0 = c1

print(len(group))            
group.sort()
print(*group)