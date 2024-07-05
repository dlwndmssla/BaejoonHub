def bk():
    if len(s) == m:
        print(' '.join(map(str,s)))
        return
    
    # print('s1',s)
    for i in range(1,n+1):
        # print('s2',s,i)
        if visited[i]:  continue
        if len(s) != 0:
            if s[-1] > i: continue
        visited[i] = True
        s.append(i)
        # print('s3_0',s)
        bk()
        # print('s3',s)
        s.pop()
        # print('s4',s)
        
        # print('v',visited)
        visited[i] = False
        # print('v1',visited)
        
n,m = map(int,input().split())
s = []
visited = [False for i in range(n+1)]

bk()