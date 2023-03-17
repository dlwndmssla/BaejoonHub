import sys
input = sys.stdin.readline
a = int(input())
ex1 = []
for i in range(a):
    b = int(input())
    
    if b !=0:
        ex1.append(b)
    else:
        ex1 = ex1[:-1]
    
print(sum(ex1))