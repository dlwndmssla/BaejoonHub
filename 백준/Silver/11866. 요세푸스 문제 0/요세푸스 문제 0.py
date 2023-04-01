import sys
input = sys.stdin.readline
a,b = map(int, input().split())

ex1 = [i for i in range(1,a+1)]
k = b-1
ans = []
while ex1:
    while k > len(ex1)-1:
        k -= len(ex1)
    ans.append(ex1[k])
    ex1.remove(ex1[k])    
    k += b-1
    
ans = ", ".join(map(str, ans))
print('<',ans,'>',sep="")