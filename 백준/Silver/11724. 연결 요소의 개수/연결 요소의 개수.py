import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(graph,v,visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(graph,i,visited)
            
n,m = map(int, input().split())
k = 0
graph = [[] for i in range(n+1)]
visited = [False for i in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    if i == 0:
        v = a
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(n+1):
    graph[i].sort()
    
for i in range(1,n+2):
    if i!=0 and visited[i] == False:
        k +=1
        dfs(graph,i,visited)        
    if sum(visited) == n:
        break
print(k)
    
    