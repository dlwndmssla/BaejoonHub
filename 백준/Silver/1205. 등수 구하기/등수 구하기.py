import sys
input = sys.stdin.readline
n, new, p = map(int, input().split())
if n != 0:
    rank = list(map(int, input().split()))
    rank.append(new)
    rank.sort(reverse=True)
    if n+1 <= p:
        print(rank.index(new)+1)
    elif rank[-1] == new:
        print(-1)
    else:
        print(rank.index(new)+1)    
else:
    print(1)