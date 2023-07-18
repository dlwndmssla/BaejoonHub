import heapq,sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline 

def dijkstra(graph,start):
    INF = 10e8
    distance = [INF for i in range(n+1)] 
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0,start))
    while queue:
        dist,now = heapq.heappop(queue)
        if distance[now] < dist: continue
        for now0,cost in graph[now]:
            dist0 = cost + dist
            if distance[now0] > dist0:
                distance[now0] = dist0
                heapq.heappush(queue, (dist0,now0))
                
    return distance
            
n,m,x = map(int,input().split())

graph = [[] for i in range(n+1)]
for i in range(m):
    u,v,w = map(int,input().split())
    graph[u].append([v,w])
    
cnt = [0]
for i in range(1,n+1):
    if i == x: continue
    route1 = dijkstra(graph,x)
    route2 = dijkstra(graph,i)
    r1 = route1[i]
    r2 = route2[x]
    cnt.append(r1+r2)

print(max(cnt))
