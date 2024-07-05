n,m = list(map(int,input().split()))

numbers = list(map(int,input().split()))
numbers.sort()
visited = [False for i in range(n)]
s = []


def bk(k):
    if (m == len(s)):
        print(" ".join(map(str,s)))
        return
    
    a = 0
    for i in range(len(numbers)):
        if visited[i]: continue
        if numbers[i] == a: continue
        visited[i] = True
        s.append(numbers[i])
        a = numbers[i]
        bk(k+1)
        s.pop()
        visited[i] = False
        
bk(0)