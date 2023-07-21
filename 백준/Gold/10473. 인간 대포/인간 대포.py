import heapq,sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def dijkstra(node,route,start):
    distance = [10e8 for i in range(len(node))] 
    distance[start] = 0
    queue = []
    heapq.heappush(queue,(0,start))
    while queue:
        dist,node = heapq.heappop(queue)
        if distance[node] < dist: continue
        for node0,cost in route[node]:
            if node == start: 
                dist0 = dist + cost/5
            else:
                dist0 = dist + 2 +abs(cost-50)/5
                
            if distance[node0] > dist0:
                distance[node0] = dist0
                heapq.heappush(queue,(dist0,node0))
    
    return distance

graph = []
x,y = map(float,input().split())
graph.append([x,y])
xend,yend = map(float,input().split())
n = int(input())

for i in range(n):
    ex = list(map(float,input().split()))
    graph.append(ex)

graph.append([xend,yend])

node = graph
route = [[] for i in range(len(node))]
for i in range(len(node)):
    a,b = node[i]
    for j in range(len(node)):
        if i == j: continue
        c,d = node[j]
        ex = pow(pow(a-c,2)+ pow(b-d,2),0.5)
        route[i].append([j,round(ex,10)])

ex = dijkstra(node,route,0)
print(ex[-1])