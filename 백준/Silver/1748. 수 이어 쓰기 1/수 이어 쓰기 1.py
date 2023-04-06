import sys
input = sys.stdin.readline
n = int(input())
x = len(str(n))
k = 0
if x == 1:
    print(n)
else:
    for i in range(1,x+1):
        if i != x:
            k += 9*pow(10,i-1)*i
        else:
            k += (n - pow(10,x-1)+1)*i
        
    print(k)