import sys
input = sys.stdin.readline

import itertools
for _ in range(int(input())):
    k,n = int(input()),int(input())
    downstair = [i for i in range(n+1)]
    for s in range(k):
        now = list(itertools.accumulate(downstair))
        # print(now)
        downstair = now
    print(now[-1])