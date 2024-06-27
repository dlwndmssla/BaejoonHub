import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline


n,m,r = list(map(int,input().split()))

graph = [[] for i in range(n+1)]

for i in range(m):
    a,b = list(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a)
    
    
for i in range(n):
    graph[i].sort()
    
visited = [False for i in range(n+1)]

route = [0 for i in range(n+1)]
count = 1
route[r] = count

def bfs(v):
    global count
    visited[v] = True
    queue = deque([v])
    while queue:
        v = queue.popleft()
        for v0 in graph[v]:
            if not visited[v0]:
                count +=1
                route[v0] = count
                visited[v0] = True
                queue.append(v0)
        
bfs(r)
for j in route[1:]:
    print(j)