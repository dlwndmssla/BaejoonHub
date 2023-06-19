import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

a,b = map(int,input().split())

max0 = 10 ** 5 +1
graph = [0 for i in range(max0)]

def bfs(graph,a,b):
    queue = deque()
    queue.append(a)
    check = False
    while queue:
        v = queue.popleft()
        for t in range(3):
            v0 = [v-1,v+1,2*v][t]
            if 0<=v0<=max0-1:
                if graph[v0] == 0 and v0 !=a:
                    graph[v0] = graph[v] + 1
                    queue.append(v0)
                    
                if v0 == b:
                    check = True
                    break
            if check: break
        if check: break

bfs(graph,a,b)
print(graph[b]) 