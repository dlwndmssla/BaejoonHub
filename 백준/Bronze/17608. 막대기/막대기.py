import sys
input = sys.stdin.readline
a = int(input())

ex1 = []
for i in range(a):
    ex1.append(int(input()))
    
ex1 = ex1[::-1]
k = max(ex1)
t = 1
n = ex1[0]
for i in range(a):
    if ex1[i] >n :
        t +=1
        n = ex1[i]
    elif n == k:
        break
    
print(t)