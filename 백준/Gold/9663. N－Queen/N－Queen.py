import sys
input = sys.stdin.readline

def check(m,queens):
    for i in range(m):
        if abs(m-i) == abs(queens[m]-queens[i]) or (queens[m]==queens[i]):        
            return False
    return True

def bk(m):
    global ans
    if m == n:
        ans+= 1
        return

    for i in range(n):
        queens[m] = i
        if not check(m,queens): continue
        bk(m+1)
        
n = int(input())

queens = [0 for i in range(n)]
ans = 0
bk(0)

print(ans)