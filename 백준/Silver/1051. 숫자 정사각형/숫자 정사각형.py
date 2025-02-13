def check_node(square,i,j):
    max0 = 0
    for w in range(n):
        if (i+w>=n) or (j+w>=m): break
        node = set([square[i][j],square[i+w][j],square[i][j+w],square[i+w][j+w]])
        if len(node) == 1: max0 = max(max0,w)
    return max0+1
            

n,m = list(map(int,input().split()))
square = [[int(j) for j in input()] for i in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans,check_node(square,i,j))
        if ans == n: break
    
print(ans**2)