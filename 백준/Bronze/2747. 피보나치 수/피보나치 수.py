import sys
input = sys.stdin.readline
a = int(input())

ex1 = [0,1]
for i in range(2,a+1):
    ex1.append(ex1[i-2]+ex1[i-1])
    
print(ex1[-1])