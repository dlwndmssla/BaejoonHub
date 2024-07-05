def bk(k):
    if len(s) == 6:
        print(*s)
        return    

    for i in range(1,len(num)):
        if visited[i]: continue
        
        if len(s) != 0:
            if s[-1] > num[i]: continue
            
        visited[i] = True
        s.append(num[i])
        bk(k+1)
        s.pop()
        visited[i] = False

while True:
    num = list(map(int,input().split()))
    s = []
    visited = [False for i in range(len(num))]
    bk(0)
    if num == [0]: break
    print('')