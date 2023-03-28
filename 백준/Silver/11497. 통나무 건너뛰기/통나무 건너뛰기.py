def logs_level(a, log):
    
    idx = []    
    log.sort()
    for i in range(a):
        if i%2 == 0:
            idx.append(int(i/2))
        else:
            idx.append(a-int(i/2)-1)
    idx.append(0)
    logs = [0]*(a)
    for j in range(a):
        logs[idx[j]] = log[j]
    logs.append(log[0])
    level = 0
    for k in range(1,a+1):
        level = max(abs(logs[k]-logs[k-1]),level)
        
    return level


n = int(input())
for _ in range(n):
    a = int(input())
    log = list(map(int, input().split()))
    print(logs_level(a, log))