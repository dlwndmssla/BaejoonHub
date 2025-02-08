import sys
input = sys.stdin.readline
n1,m1 = list(map(int,input().split()))
list1 = [list(map(int,input().split())) for i in range(n1)]
n2,m2 = list(map(int,input().split()))
list2 = [list(map(int,input().split())) for i in range(n2)]
list3 = [list(i) for i in zip(*list2)]
# print(list1)
# print(list2)
# print(list3)

ans = [[ sum([x[0]*x[1] for x in zip(i,j)]) for i in list3] for j in list1]
for i in ans:
    print(*i)