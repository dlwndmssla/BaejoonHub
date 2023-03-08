N, M = map(int, input().split())
exam = [0 for i in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    for j in range(a-1,b):
        exam[j] = c
        
print(*exam)