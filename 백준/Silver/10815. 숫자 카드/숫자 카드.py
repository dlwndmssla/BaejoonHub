#list의 시간복잡도는 O(n)이고 set의 시간복잡도는 O(1)이다.
import sys
input = sys.stdin.readline
N = int(input())
exam1 = set(map(int,input().split()))
M = int(sys.stdin.readline())
exam2 = list(map(int,input().split()))
exam3 = [0 for i in range(M)]
for i in range(M):
    if exam2[i] in exam1:
        exam3[i] = 1

print(*exam3)