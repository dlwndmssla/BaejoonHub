import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

a = int(input())

def func(n):
    if n in (1,2):
        return n
    elif n == 3:
        return 4
    else:
        return func(n-1)+func(n-2)+func(n-3)
    
for i in range(a):
    n = int(input())
    print(func(n))