def bk():
    if len(s) == m:
        print(' '.join(map(str,s)))
        return
    
    # print('s1',s)
    for i in range(1,n+1):
        s.append(i)
        bk()
        s.pop()
        visited[i] = False
        
n,m = map(int,input().split())
s = []
visited = [False for i in range(n+1)]

bk()