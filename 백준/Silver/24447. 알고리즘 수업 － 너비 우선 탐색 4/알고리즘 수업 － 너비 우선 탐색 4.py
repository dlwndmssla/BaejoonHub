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

visited = [False for i in range(n+1)]

depth = [0 for i in range(n+1)]

def bfs(v):
    global count
    visited[v] = True
    p = depth[v] 
    queue = deque([[v,p]])
    while queue:
        v,p = queue.popleft()
        for v0 in graph[v]:
            if visited[v0]: continue
            depth[v0] = p+1
            visited[v0] = True
            count +=1
            route[v0] = count
            queue.append([v0,p+1])
        
bfs(r)

print(sum([depth[j]*route[j] for j in range(n+1)]))