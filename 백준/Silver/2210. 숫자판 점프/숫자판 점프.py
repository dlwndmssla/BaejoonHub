   
import sys
sys.setrecursionlimit(10 ** 9)

def bk(idx, n):
    global ans 
    if len(s) == 6:
        s_str = ''.join(map(str, s))
        if s_str not in s0:
            s0.add(s_str)
            ans += 1
        return
    
    for i in [n-5, n-1, n+1, n+5]:
        if not (0 <= i <= 24): continue
        if n % 5 == 0 and i == n-1: continue 
        if n % 5 == 4 and i == n+1: continue  

        s.append(world[i])
        bk(idx + 1, i)
        s.pop()

world = []

for _ in range(5):
    world += list(map(int, input().split())) 

s = []
s0 = set()
ans = 0

for k in range(25):
    s.append(world[k])
    bk(0, k)
    s.pop()

print(ans)
