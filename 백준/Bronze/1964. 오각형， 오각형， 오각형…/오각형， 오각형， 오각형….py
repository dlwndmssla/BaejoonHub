import sys
input = sys.stdin.readline
n = int(input())
k = 1

for i in range(1,n+1):
    k += 3*i+1
    
print(k%45678)