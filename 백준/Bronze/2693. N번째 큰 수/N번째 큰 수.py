n = int(input())

for i in range(n):
    ex = list(map(int,input().split()))
    ex.sort()
    print(ex[-3])
