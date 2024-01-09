a1,a0 = map(int,input().split())
c = int(input())
n0 = int(input())
print(int((a0<=n0*(c-a1))*(a1<=c)))