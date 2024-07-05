n,m = list(map(int,input().split()))

numbers = list(map(int,input().split()))
numbers.sort()
visited = [False for i in range(n)]
s = []
def bk(k):
    if m == len(s):
        print(" ".join(map(str,s)))
        return
    
    for i in range(len(numbers)):
        if visited[i]: continue
        visited[i] = True
        s.append(numbers[i])
        bk(k+1)
        s.pop()
        visited[i] = False
        
bk(0)