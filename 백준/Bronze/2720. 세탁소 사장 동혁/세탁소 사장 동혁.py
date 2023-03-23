import sys
input=sys.stdin.readline
a = int(input())
coin = [25,10,5,1]
for i in range(a):
    k = int(input())
    ex1= [ ]
    for j in range(4):
        ex1.append(int(k/coin[j]))
        k = k%coin[j]
        
    print(*ex1)