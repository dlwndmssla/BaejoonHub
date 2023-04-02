import sys, math
input = sys.stdin.readline
a = math.sqrt(int(input()))
b = math.sqrt(int(input()))
a = math.ceil(a)
b = math.floor(b)
if a > b:
    print(-1)
else:
    k = 0
    ex = []
    for i in range(a,b+1):
        k += i*i    
    print(k)
    print(a*a)