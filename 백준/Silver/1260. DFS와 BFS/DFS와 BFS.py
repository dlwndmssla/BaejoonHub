import sys
from collections import deque

# DFS 구현
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# BFS 구현
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 입력 처리
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i].sort()

# DFS, BFS 호출
visited = [False] * (n+1)
dfs(graph, v, visited)
print()
visited = [False] * (n+1)
bfs(graph, v, visited)