import sys
input = sys.stdin.readline
n = int(input())
x = int(n/7)
if n >= 28:
    while True:
        y = x*7
        if y >= n:
            print(x+3)
            break
        else:
            x += 1
else:
    k = 0
    for i in range(1,8):
        k += i
        if k >= n: 
            print(i)
            break