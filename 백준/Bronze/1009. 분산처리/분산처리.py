import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    a,b = map(int,input().split())
    a = a%10
    if a in {1,5,6}:
        print(a)
    elif a == 0:
        print(10)
    elif a in {2,3,7,8}:
        b = (b-1)%4+1
        print(pow(a,b)%10)
    else:
        b = (b-1)%2+1
        print(pow(a,b)%10)