import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
graph = [0]
graph += list(map(int, input().split()))
a,b = map(int, input().split())

def bfs(graph, v, visited):
    break_check = False
    visited[v] = True
    queue = deque([v])
    while queue:
        v = queue.popleft()
        for i in range(1,n+1):
            if not visited[i]:
                if (v-i)%graph[v] == 0:
                    visited[i] = True
                    queue.append(i)
                    c0[i] = c0[v] + 1
                    if i == b:
                        break_check = True
        if break_check:
            break
                    
visited = [False for i in range(n+1)]
v = a
c0 = [0 for i in range(n+1)]
bfs(graph,v,visited)

if c0[b] != 0:
    print(c0[b])
elif a == b:
    print(0)
else:
    print(-1)