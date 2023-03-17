import sys
input = sys.stdin.readline
a = int(input())

def f(x) :
    return (x*(x+1)/2)
    
i = 0
while True:
    c = f(i)
    d = f(i+1)
    if a == 1:
        print(1)
        break
    elif  c*6+2 <= a <= d*6+1 :
        print(i+2)
        break
    i += 1  