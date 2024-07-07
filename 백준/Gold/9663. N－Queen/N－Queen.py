def check(v,queens):
    y,x = v
    for i in range(len(queens)):
        if abs(y-i) == abs(x-queens[i]):        
            return False
    return True

def bk(m):
    global ans
    if m == n:
        ans+= 1
        return
    
    for i in range(n):
        if visited[i]: continue
        if not check([m,i],queens): continue
        
        visited[i] = True
        queens.append(i)
        bk(m+1)
        queens.pop()
        visited[i] = False
        
n = int(input())

queens = []

visited = [False for i in range(n)]
ans = 0

bk(0)

print(ans)