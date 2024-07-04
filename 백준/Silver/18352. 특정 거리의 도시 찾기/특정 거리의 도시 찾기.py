import sys, heapq
input = sys.stdin.readline 

n,m,k,x = list(map(int,input().split()))
INF = 1e8
graph = [ [] for i in range(n+1) ]
distance = [ INF for i in range(n+1) ]
for i in range(m):
    a,b = list(map(int,input().split()))
    graph[a].append((b,1))

import heapq

def dijkstra(graph,x):
    distance[x] = 0
    queue = []
    heapq.heappush(queue, (0, x)) # 우선순위, 값 형태로 들어간다.
    while queue:
        dist,now = heapq.heappop(queue)
        for now0,cost in graph[now]:
            dist0 = distance[now]+cost
            if dist0 >= distance[now0]: continue
            distance[now0] = dist0
            heapq.heappush(queue, (dist0, now0))

    return distance

dist1 = dijkstra(graph,x)

if dist1[1:].count(k) > 0:
    for i in range(1,len(dist1)):
        if dist1[i] == k:
            print(i)
else:
    print(-1)
