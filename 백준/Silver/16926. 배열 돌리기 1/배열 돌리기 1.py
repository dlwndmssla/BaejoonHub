import sys
input=sys.stdin.readline

n,m,r = map(int,input().split())
graph = []
for i in range(n):
    ex = list(map(int,input().split()))
    graph.append(ex)
    
graph0 = [[0 for i in range(m)] for i in range(n)]


for i in range(int(n/2)):
    for j in range(m):
        if j > i and i+j <m:
            graph0[i][j] = 1

for i in range(n):
    for j in range(int(m/2)):
        if i+j < n-1 and graph0[i][j] == 0:
            graph0[i][j] = 3
            
for i in range(int(n/2),n):
    for j in range(m):
        if j-i < m-n and graph0[i][j] == 0:
            graph0[i][j] = 2
            
for i in range(n):
    for j in range(int(m/2),m):
        if graph0[i][j] == 0:
            graph0[i][j] = 4
            
if n == m and n%2 == 1:
    graph0[int(n/2)][int(n/2)] = 0
    
if n < m and n%2 == 1:
    a = int(n/2)
    for i in range(m):
        if m-2*i == m-n+1:
            graph0[a][i:m-i] = [0]*(m-n+1)

if n > m and m%2 == 1:
    a = int(m/2)
    for i in range(n):
        if n-2*i == n-m+1:
            graph0[a][i:n-i] = [0]*(n-m+1)        
            
for i in range(r):
    graph1 = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if graph0[i][j] == 1:
                graph1[i][j-1] = graph[i][j]
            elif graph0[i][j] == 2:
                graph1[i][j+1] = graph[i][j]
            elif graph0[i][j] == 3:
                graph1[i+1][j] = graph[i][j]
            elif graph0[i][j] == 4: 
                graph1[i-1][j] = graph[i][j]
    graph = graph1
    
for q in range(n):
    print(*graph[q])