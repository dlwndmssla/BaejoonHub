n = int(input())
graph = []
for i in range(n):
    graph.append(str(input()))
    
graph1 = [[0 for i in range(len(graph[0]))] for j in range(n)]
graph2 = [[0 for i in range(len(graph[0]))] for j in range(n)]

a,b = 0,0
for i in range(n):
    for j in range(len(graph[0])):
        if graph[i][j] == '.':
            graph1[i][j] = graph1[i][j-1] +1 
            graph2[i][j] = graph2[i-1][j] +1 
            if graph1[i][j] == 2:
                a += 1
            if graph2[i][j] == 2:
                b += 1

print(a,b)