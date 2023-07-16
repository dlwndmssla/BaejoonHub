import sys, heapq
input = sys.stdin.readline 

n,m = map(int,input().split())

start = int(input())

graph = [[] for i in range(n+1)]

for i in range(m):
    u,v,w = map(int,input().split())
    graph[u].append([v,w])

def dijkstra(graph,start):
    INF = -1
    distance = [INF]*(n+1)
    distance[start] = 0
    
    queue = []
    heapq.heappush(queue,(0,start))
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist and distance[now] != -1: continue
        for now0,cost in graph[now]:
            dist0 = dist + cost
            if distance[now0] > dist0 or distance[now0] == -1:
                distance[now0] = dist0
                heapq.heappush(queue, (dist0, now0))
                
    return distance
            
distance = dijkstra(graph,start)[1:]

for i in range(n):
    if distance[i] != -1:
        print(distance[i])
    else:
        print('INF')