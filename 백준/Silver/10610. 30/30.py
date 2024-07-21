
import sys
input = sys.stdin.readline 

nlist0 = list(map(int, input().strip()))

con1 = 0 in nlist0

con2 = sum(nlist0) % 3 == 0


if con1 and con2:
    nlist0.sort(reverse=True)
    result = int(''.join(map(str, nlist0)))
    print(result)
else:
    print(-1)