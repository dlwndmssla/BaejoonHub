max0 = 0
now = 0
for i in range(10):
    a,b = map(int,input().split())
    now -= a
    now += b
    max0 = max(max0,now)
print(max0)