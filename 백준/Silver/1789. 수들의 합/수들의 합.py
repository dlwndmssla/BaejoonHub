import sys
input = sys.stdin.readline
a = int(input())
i = 1
while 1:
    b = a - i*(i+1)/2
    if b < 0 :
        break
    i += 1
    
print(i-1)