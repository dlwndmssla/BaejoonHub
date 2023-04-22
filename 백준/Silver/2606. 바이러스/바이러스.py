import sys
input = sys.stdin.readline
def dfs(graph,v,visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(graph,i,visited)
n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
visited = [False for i in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i].sort()
dfs(graph,1,visited)
print(sum(visited)-1)