import heapq,sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline 

def dijkstra(graph,start):
    INF = 10e8
    distance = [[INF for i in range(n)] for j in range(n)]
    y,x = start
    distance[y][x] = 0
    queue = []
    heapq.heappush(queue, (0,start))
    while queue:
        dist,now = heapq.heappop(queue)
        y,x = now
        if distance[y][x] < dist: continue
        for t in range(4):
            y0,x0 = y + [-1,1,0,0][t], x + [0,0,-1,1][t]
            now0 = [y0,x0]
            if 0 <= y0 <= n-1 and 0 <= x0 <= n-1:
                cost = graph[y0][x0]
                dist0 = dist + cost
                if distance[y0][x0] > dist0:
                    distance[y0][x0] = dist0
                    heapq.heappush(queue, (dist0,now0))

    return distance

n = int(input())

graph = []
for i in range(n):
    ex = list(map(str,input().rstrip()))
    for j in range(n):
        if ex[j] == '1':
            ex[j] = 0
        else:
            ex[j] = 1
    graph.append(ex)
    
start = [0,0]

distance0 = dijkstra(graph,start)

print(distance0[-1][-1])

    