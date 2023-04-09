import sys
input = sys.stdin.readline
ex = ['push','pop','size','empty','front','back']
n = int(input())
queue = []
for i in range(n):
    x = list(input().split())
    y = ex.index(x[0])
    if y== 0:
        queue.append(x[1])        
    elif y== 1:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue = queue[1:]      
    elif y== 2:
        print(len(queue))        
    elif y== 3:
        if len(queue) == 0:
            print(1)
        else:
            print(0)        
    elif y== 4:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])