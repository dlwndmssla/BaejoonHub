import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

n,m = map(int, input().split())
graph = []
water = []
for i in range(n):
    ex = list(map(str,input().rstrip()))
    for j in range(m):
        if ex[j] == 'S':
            hedgehog = [i,j]
        elif ex[j] == '*':
            water.append([i,j])
        elif ex[j] == 'D':
            beaver = [i,j]
    graph.append(ex)

def bfs(graph,water,hedgehog):
    queue = deque(water)
    queue.append(hedgehog)
    while queue:
        v = queue.popleft()
        y,x = v
        if [y,x] in water:
            graph[y][x] = [0,'*']
        elif [y,x] == hedgehog:
            graph[y][x] = [0,'S'] 
        for t in range(4):
            x0, y0 = x + [-1,1,0,0][t], y + [0,0,-1,1][t]
            if  0 <= x0 <= m-1 and 0 <= y0 <= n-1:
                if graph[y0][x0] == '.':
                    graph[y0][x0] = [graph[y][x][0]+1,graph[y][x][1]]
                    queue.append([y0,x0])
                if graph[y0][x0] == 'D' and graph[y][x][1] == 'S':
                    graph[y0][x0] = [graph[y][x][0]+1,graph[y][x][1]]
                    return graph
    return graph

graph0 = bfs(graph,water,hedgehog)
ans = graph0[beaver[0]][beaver[1]]
if type(ans) == list:
    print(ans[0])
else:
    print("KAKTUS")
            