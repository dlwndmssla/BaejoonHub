import sys
input = sys.stdin.readline
a = int(input())
ex1 = list(map(int, input().split()))
ex3 = list(map(int, input().split()))
if set(ex3) != {ex3[0]}:
    for i in range(a-1):
        for j in range(i,a-1):
            if ex3[j] < ex3[i]:
                break
            else:
                ex3[j] = ex3[i]
    cost = 0
    for i in range(a-1):
        cost += ex3[i]*ex1[i]
        
    print(cost)
else:
    print(sum(ex1))