import sys
input = sys.stdin.readline

for i in range(int(input())):
    input()
    ex = list(map(int,input().split()))
    a = ex[3]
    ex = ex[0:3]
    if a !=0:
        for j in range(a):
            ex.sort()
            ex[-1] -= 1
        print(ex[0]*ex[1]*ex[2])

    else:
        print(ex[0]*ex[1]*ex[2])