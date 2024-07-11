import sys
# input = sys.stdin.readine

from collections import deque

def bk(idx,start, cnt):
    global result
    if cnt >= 4: return
    if idx == 7:
        if bfs():
            result += 1
        return
        
    for i in range(start,25):
        r,c = i//5,i%5
        s.append((r,c))
        bk(idx+1,i+1,cnt+(seats[r][c] == 'Y'))
        s.pop()
        
def bfs():
    dy,dx = [-1,1,0,0],[0,0,-1,1]
    visited = [[1 for i in range(5)] for j in range(5)]
    for v in s:
        visited[v[0]][v[1]] = 0
    
    queue = deque([s[0]])
    visited[s[0][0]][s[0][1]] = 1
    check = 1
    while queue:
        y,x = queue.popleft()
        for t in range(4):
            y0,x0 = y+dy[t],x+dx[t]
            if not (0<= y0 <=4 and 0<= x0 <=4): continue
            if visited[y0][x0]: continue
            visited[y0][x0] = 1
            check += 1
            queue.append((y0,x0))
            
    return (check == 7)
                

seats = [ list(map(str,input())) for i in range(5)]
s = []
result = 0
bk(0,0,0)
print(result)
        