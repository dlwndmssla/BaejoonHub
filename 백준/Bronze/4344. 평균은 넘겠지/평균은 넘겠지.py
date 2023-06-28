import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    ex = list(map(int,input().split()))
    x = sum(ex[1:])/ex[0]
    cnt = 0
    for j in range(ex[0]):
        if ex[j+1] > x:
            cnt += 1
            
    print('{:.3f}%'.format(round(cnt*100/ex[0],3)))
        