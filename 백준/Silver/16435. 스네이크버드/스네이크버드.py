import sys
input=sys.stdin.readline
N,L = map(int, input().split())

fruits = list(map(int, input().split()))
fruits.sort()

for height in fruits:
    if height <= L:
        L += 1
    else:
        break
    
print(L)