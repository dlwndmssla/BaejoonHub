import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
a,b = map(int, input().split())
m = int(input())
graph = [[] for i in range(n+1)]

for i in range(m):
    ex0,ex1 = map(int, input().split())
    graph[ex0].append(ex1)
    graph[ex1].append(ex0)

def dfs(graph, v, parent, visited):
    visited[v] = True
    x0 = v
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            parent[i] = v
            dfs(graph, i, parent, visited)

v = a

visited = [False for i in range(n+1)]
parent = [0 for i in range(n+1)]

dfs(graph, v, parent, visited)

if parent[b] != 0:
    k = 0
    t = b
    for i in range(m):
        t = parent[t]
        k += 1
        if t == a:
            break
    print(k)
else:
    print(-1)
