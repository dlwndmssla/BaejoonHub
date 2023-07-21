import heapq,sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def dijkstra(graph,start):
    distance = [10e8 for i in range(n+1)]
    distance[start] = 0
    queue = []
    heapq.heappush(queue,(0,start)) #dist,node
    while queue:
        dist,node = heapq.heappop(queue)
        if distance[node] < dist: continue
        for node0,cost in graph[node]:
            dist0 = dist + cost
            if distance[node0] > dist0:
                distance[node0] = dist0
                heapq.heappush(queue,(dist0,node0))
                
    return distance

n,m,r = map(int,input().split())


item = list(map(int,input().split()))
graph = [[] for i in range(n+1)]

for i in range(r):
    u,v,w = map(int,input().split())
    graph[u].append([v,w])
    graph[v].append([u,w])
    
max0 = 0
for i in range(1,n+1):
    value = dijkstra(graph,i)
    cnt = 0
    for j in range(1,n+1):
        if value[j] <= m:
            cnt += item[j-1]
        
    max0 = max(cnt,max0)
    if max0 == sum(item): break
    
print(max0)