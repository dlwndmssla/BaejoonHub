# 젤다
import heapq,sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline 

def dijkstra(graph):
    inf = 10e8
    distance = [[ inf for i in range(n)] for j in range(n)]
    distance[0][0] = graph[0][0]
    queue = []
    heapq.heappush(queue,(graph[0][0],[0,0]))
    
    while queue:
        dist,now = heapq.heappop(queue)
        y,x = now
        if distance[y][x] < dist: continue
        for t in range(4):
            y0,x0 = y + [-1,1,0,0][t] , x + [0,0,-1,1][t]
            if 0 <= x0 <= n-1 and 0 <= y0 <= n-1:
                now0 = [y0,x0]
                cost = graph[y0][x0]
                dist0 = dist + cost
                if distance[y0][x0] > dist0 :
                    distance[y0][x0] = dist0
                    heapq.heappush(queue,(dist0,now0))

    return distance

cnt = 1
while True:
    n = int(input())
    if n == 0: break
    
    graph = []
    for i in range(n):
        ex = list(map(int,input().split()))
        graph.append(ex)
    
    distance0 = dijkstra(graph)
    print('Problem {}: {}'.format(cnt, distance0[-1][-1]))
    cnt += 1  
    