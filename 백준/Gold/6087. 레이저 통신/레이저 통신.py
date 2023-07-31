import sys,heapq
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def mirror(dir,dir0,x,y):
    if [y,x] == Laser or dir == dir0:
        return 0
    elif set([dir,dir0]) in [set([1,2]),set([3,4])]:
        return 2
    else: return 1   

def dijkstra(graph,start):
    dir_graph = [[0 for i in range(m)] for j in range(n)]
    y,x = start
    graph[y][x] = 0
    queue = []
    heapq.heappush(queue, (0,start))
    while queue:
        dist,now = heapq.heappop(queue)
        y,x = now
        if graph[y][x] == '*': continue
        if graph[y][x] < dist: continue
        for t in range(4):
            y0,x0 = y , x 
            while True:   
                y0,x0 = y0 + [0,0,-1,1][t], x0 + [-1,1,0,0][t]
                if 0 <= y0 <= n-1 and 0 <= x0 <= m-1:
                    if graph[y0][x0] == '*': break
                    dir,dir0 = dir_graph[y][x],t+1
                    dist0 = graph[y][x] + mirror(dir,dir0,x,y)
                    if graph[y0][x0] > dist0:
                        graph[y0][x0] = dist0
                        dir_graph[y0][x0] = dir0
                        heapq.heappush(queue, (dist0,[y0,x0]))
                else: break
                    
    return dir_graph, graph


m,n = map(int, input().split())

graph = []
Laser = []

inf = int(10e8)

for i in range(n):
    ex = list(map(str, input().rstrip()))
    for j in range(m):
        if ex[j] == '.':
            ex[j] = int(inf)
        elif ex[j] == 'C': 
            ex[j] = int(inf)
            if len(Laser) == 0:
                Laser = [i,j]
            else:
                endy,endx = [i,j]
        
    graph.append(ex)        

dir_graph0, graph0 = dijkstra(graph,Laser)
print(graph0[endy][endx])