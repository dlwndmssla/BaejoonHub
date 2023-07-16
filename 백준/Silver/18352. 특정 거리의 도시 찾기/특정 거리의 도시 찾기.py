import sys, heapq
input = sys.stdin.readline

n,m,k,x = map(int,input().split())
INF = int(10e8)
graph = [[] for i in range(n+1)]

for i in range(m):
    u,v= map(int,input().split())
    if [v,1] not in graph[u]:
        graph[u].append([v,1])

def dijkstra(start):
    distances = [INF] * (n+1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (distances[start], start))
    while queue:
        dist, now = heapq.heappop(queue)
        if distances[now] < dist:
            continue
        for now0, weight in graph[now]:
            dist0 = dist + weight
            if dist0 < distances[now0]:
                distances[now0] = dist0
                heapq.heappush(queue, (dist0, now0))

    return distances

distances = dijkstra(x)

if distances[1:].count(k) > 0:
    for i in range(1,len(distances)):
        if distances[i] == k:
            print(i)
else:
    print(-1)