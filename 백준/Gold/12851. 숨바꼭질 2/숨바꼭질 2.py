from collections import deque

def bfs(n, k):
    visited = [-1] * 100001  
    count = [0] * 100001 
    queue = deque()
    queue.append(n)
    visited[n] = 0  
    count[n] = 1 

    while queue:
        v = queue.popleft()

        if v == k:
            return visited[v], count[v]


        for v0 in (v-1, v+1, 2*v):
            if 0 <= v0 <= 100000:
    
                if visited[v0] == -1:
                    visited[v0] = visited[v] + 1
                    count[v0] = count[v]
                    queue.append(v0)

                elif visited[v0] == visited[v] + 1:
                    count[v0] += count[v]

    return -1, 0

n, k = map(int, input().split())
shortest_time, num_ways = bfs(n, k)
print(shortest_time)
print(num_ways)