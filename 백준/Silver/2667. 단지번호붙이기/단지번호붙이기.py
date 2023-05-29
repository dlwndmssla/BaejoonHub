import sys
sys.setrecursionlimit(10 ** 6)
#input = sys.stdin.readline

n = int(input())

graph = []
for i in range(n):
    ex = list(map(int, input().rstrip()))
    graph.append(ex)

visited = [[False for i in range(n)] for i in range(n)]

def dfs(graph,x,y,visited):
    visited[y][x] = True
    for t in range(4):
        x0 = [0,0,-1,1][t] + x
        y0 = [-1,1,0,0][t] + y
        if 0<=y0<=n-1 and 0<=x0<=n-1 and graph[y0][x0] == 1: 
            if not visited[y0][x0]:
                visited[y0][x0] = True
                dfs(graph,x0,y0,visited)

count0 = 0

count_list = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == False:
            x,y = j,i
            dfs(graph,x,y,visited)
            count1 = sum([sum(visited[q]) for q in range(len(visited))])
            count_list.append(count1-count0)
            count0 = count1

count_list.sort()
print(len(count_list))       
for i in range(len(count_list)):
    print(count_list[i])