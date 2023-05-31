import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())

graph = [[] for i in range(n+1)]
visited = [False for i in range(n+1)]
parent = [0 for i in range(n+1)]

for i in range(n-1):
    a,b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph,v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            parent[i] = v
            dfs(graph,i,visited)
            
for j in range(1,n+1):
    if visited[j] == False:
        v = j
        dfs(graph,v,visited)

for k in range(2,len(parent)):
    print(parent[k])