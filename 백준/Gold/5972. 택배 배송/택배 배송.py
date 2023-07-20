import heapq,sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline 

def dijkstra(graph):
    distance = [10e8 for i in range(n+1)]
    distance[1] = 0
    queue = []
    heapq.heappush(queue,(0,1))
    
    while queue:
        dist,node=heapq.heappop(queue)
        if distance[node] < dist: continue     
        for node0,cost in graph[node]:
            dist0 = dist + cost
            if distance[node0] > dist0:
                distance[node0] = dist0
                heapq.heappush(queue,(dist0,node0))
    
    
    return distance

n,m = map(int,input().split())

graph = [[] for i in range(n+1)]
for i in range(m):
    a,b,w = map(int,input().split())
    graph[a].append([b,w])
    graph[b].append([a,w])
ans = dijkstra(graph)
print(ans[-1])