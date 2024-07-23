import sys
input = sys.stdin.readline

def bk(m):
    if len(s) == l:
        vowels = sum([ s0 in s for s0 in ['a','e','i','o','u']])
        consonants = l-vowels
        if vowels >= 1 and consonants >= 2:
            print(''.join(map(str,s)))
        return
    
    for i in range(m,c):
        if visited[i]: continue
        if len(s) != 0:
            if s_idx[-1] > i: continue
        visited[i] = True
        s.append(str_list[i])
        s_idx.append(i)
        bk(m+1)
        s.pop()
        s_idx.pop()
        visited[i] = False
        
l,c = list(map(int,input().split()))
str_list = sorted(list(map(str,input().split())))


s = []
s_idx = []
visited = [False for i in range(c)]

bk(0)