out0, in0 = map(int,input().split())

total0 = out0+in0
if total0%2 == 0:
    for x in range(2,int(out0/2)+1,2):
        y = int(out0/2)-x+2
        if x*y == total0:
            print(max(x,y),min(x,y))
            break
else:
    for x in range(1,int(out0/2)+1,2):
        y = int(out0/2)-x+2
        if x*y == total0:
            print(max(x,y),min(x,y))
            break