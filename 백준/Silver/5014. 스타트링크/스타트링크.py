import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

f,s,g,u,d = map(int,input().split())

graph = [0 for i in range(f+1)]
def bfs(f,s,u,d,graph):
    queue = deque()
    queue.append(s)
    check = False
    while queue:
        v = queue.popleft()
        for t in [u,-d]:
            v1 = v + t
            if 1<= v1 <= f:
                if graph[v1] == 0 and v1 != s:
                    graph[v1] = graph[v] + 1
                    queue.append(v1)

if s == g:
    print(0)
else:     
    bfs(f,s,u,d,graph)                
    if graph[g] > 0:
        print(graph[g])
    else:
        print('use the stairs')
