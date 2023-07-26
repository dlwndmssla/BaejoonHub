import sys,heapq
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def dijkstra(graph,s):
    inf = 10e8
    distance = [ inf for i in range(n+1) ]
    distance[s] = 0
    queue = []
    heapq.heappush(queue,(0,s))
    while queue:
        dist,node = heapq.heappop(queue)
        if distance[node] < dist: continue
        for node0, cost in graph[node]:
            dist0 = dist + cost    
            if distance[node0] > dist0:
                distance[node0] = dist0
                heapq.heappush(queue,(dist0,node0))
                
    return distance

a = int(input())
for p in range(a):
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())

    graph0 = [[] for i in range(n+1)]
    graph1 = [[] for i in range(n+1)]
    destination = []
    
    for i in range(m):
        u,v,w = map(int,input().split())
        graph0[u].append([v,w])
        graph0[v].append([u,w])
        if set([g,h]) == set([u,v]):
            road = w
            continue
        graph1[u].append([v,w])
        graph1[v].append([u,w])
    for i in range(t):
        b = int(input())
        destination.append(b)
        
    case1 = dijkstra(graph0,s)
    case2 = dijkstra(graph1,s)

    #print(case1[1:])
    #print(case2[1:])

    ans = []
    #print(destination)
    for c in destination:
        if case1[c] < case2[c]:
            ans.append(c)
        elif case1[c] == case2[c]:
            test = dijkstra(graph0,c)
            ex1 = case1[g] + road + test[h]
            ex2 = case1[h] + road + test[g]
            ex0 = min(ex1,ex2)
            if ex0 == case1[c]:
                ans.append(c)      
            
    ans.sort()
    print(*ans)
