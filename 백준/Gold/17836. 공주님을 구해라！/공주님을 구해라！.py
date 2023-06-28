import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

n,m,t = map(int, input().split())

graph = []

for i in range(n):
    ex = list(map(int, input().split()))
    for j in range(m):
        if ex[j] == 1:
            ex[j] = '#'
        elif ex[j] == 2:
            ex[j] = -1
            sword = [i,j]
        else:
            ex[j] = -1
    graph.append(ex)
    
def bfs(graph,sword):
    v = [0,0]
    queue = deque()
    queue.append(v)
    y,x = v
    graph[y][x] = 0
    while queue:
        v = queue.popleft()
        y,x = v
        for k in range(4):
            x0 = x + [-1,1,0,0][k]
            y0 = y + [0,0,-1,1][k]
            
            if 0 <= x0 <= m-1 and 0 <= y0 <= n-1:
                if graph[y0][x0] == -1:
                    graph[y0][x0] = graph[y][x] + 1
                    v0 = [y0,x0]
                    queue.append(v0)
                    
    return graph[sword[0]][sword[1]], graph[-1][-1]

sword0, princess = bfs(graph,sword)
sword_princess = sword0 + abs(sword[0]- (n-1)) + abs(sword[1]- (m-1))

if sword0 != -1 and princess != -1:
    if min(sword_princess,princess) <= t:
        print(min(sword_princess,princess))
    else:
        print("Fail")
elif sword0 == -1 and princess != -1:
    if princess <= t:
        print(princess)
    else:
        print("Fail")
elif sword0 != -1 and princess == -1:
    if sword_princess <= t:
        print(sword_princess)
    else:
        print("Fail")
elif sword0 == -1 and princess == -1:
    print("Fail")