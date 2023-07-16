import sys, heapq
input = sys.stdin.readline 

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]

for i in range(m):
    u,v,w = map(int,input().split())
    graph[u].append([v,w])
    
start,end = map(int,input().split())

def dijkstra(graph,start):
    INF = int(10e8)
    distance = [INF]*(n+1)
    distance[start] = 0
    
    queue = []
    heapq.heappush(queue,(0,start))
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist: continue
        for now0,cost in graph[now]:
            dist0 = dist + cost
            if distance[now0] > dist0:
                distance[now0] = dist0
                heapq.heappush(queue, (dist0, now0))
                
    return distance
            
distance = dijkstra(graph,start)[end]

print(distance)