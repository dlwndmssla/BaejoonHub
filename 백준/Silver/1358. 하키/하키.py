import sys
input = sys.stdin.readline

w,h,x,y,p = list(map(int,input().split()))

player = [list(map(int,input().split())) for i in range(p)]

r = h/2

ans = 0
for x0,y0 in player:
    # print(x0,y0)
    con1 = pow(pow(x-x0,2)+pow(y+r-y0,2),0.5) <= r
    # print('con1',con1)
    con2 = pow(pow(x+w-x0,2)+pow(y+r-y0,2),0.5) <= r
    # print('con2',con2)
    con3 = (x<= x0<=x+w) & (y<= y0<= y+h)
    # print('con3',con3)
    
    con = con1 or con2 or con3
    if con: ans += 1
    
print(ans)