import sys
input = sys.stdin.readline
while True:
    
    a = list(map(int, input().split()))
    a.sort()
    if max(a) == min(a) == 0 :
        break
    elif pow(a[0],2)+pow(a[1],2) == pow(a[2],2):
        print('right')
    else:
        print('wrong')
        