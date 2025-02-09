import sys
input = sys.stdin.readline

n,l = list(map(int,input().split()))
blinker = [list(map(int,input().split())) for i in range(n)]
# print(blinker)
now,d0 = 0,0
for d,r_time,d_time in blinker:
    now += d-d0
    # print([d,r_time,d_time],now,d,d0,d,d0)
    
    cycle = r_time+d_time
    if now%cycle < r_time:
        # print(now,cycle,now%cycle)
        # print(r_time - now%cycle)
        now += r_time - now%cycle
    d0 = d
    
now += l-d
print(now)