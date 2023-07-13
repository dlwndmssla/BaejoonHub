import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def dist(dir,dir0):
    if dir == dir0:
        dist0 = 1
    elif set([dir,dir0]) in [set([1,2]),set([3,4])]:
        dist0 = 3
    else:
        dist0 = 2
    
    return dist0

def bfs(graph,start,end):
    queue = deque()
    queue.append(start)
    end_list = []
    while queue:
        v = queue.popleft()
        y,x,dir = v
        for k in [1,2,3]:
            for t in range(4):
                y0,x0,dir0 = y + [0,0,k,-k][t],x + [k,-k,0,0][t], t+1
                v0 = [y0,x0,dir0]
                if 0 <= x0 <= m-1 and 0 <= y0 <= n-1:
                    type0 = [ graph[y + [0,0,s,-s][t]][x + [s,-s,0,0][t]][0] for s in range(1,k+1)]
                    if '#' not in type0:        
                        dist0 = dist(dir,dir0)    

                        if [y0,x0] == end[0:2] and [graph[y][x][0] +dist0,dir0] not in end_list and dir == graph[y][x][1]:
                            end_list.append([graph[y][x][0] +dist0,dir0])

                        if graph[y0][x0][0] == -1 or graph[y0][x0][0] > graph[y][x][0] +dist0:
                            if dir == graph[y][x][1]:
                                graph[y0][x0] = [graph[y][x][0] +dist0,dir0]
                                queue.append(v0)                   

    return graph,end_list

n,m = map(int,input().split())
graph = []

for i in range(n):
    ex = list(map(int,input().split()))
    for j in range(m):
        if ex[j] == 1:
            ex[j] = ['#',0]
        else:
            ex[j] = [-1,0]
    graph.append(ex)
    
start = list(map(int,input().split()))
end = list(map(int,input().split()))
if start[0:2] != end[0:2]:
    start[0],start[1] =start[0]-1,start[1]-1
    end[0],end[1] =end[0]-1,end[1]-1
    graph[start[0]][start[1]] = [0,start[-1]]
    graph,end_list = bfs(graph,start,end)     
    end0 = end[-1]
    cnt = []
    for i in range(len(end_list)):
        cnt0 = end_list[i][0] + dist(end_list[i][1], end0)-1
        cnt.append(cnt0)
    print(min(cnt))
else:
    print(dist(start[-1],end[-1])-1)