ex = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ex1 = [ 0 for i in range(26)]

n = int(input())
for i in range(n):
    a = str(input())
    ex1[ex.index(a[0])] += 1
    
ans = ''
for j in range(26):
    if ex1[j]>=5:
        ans += ex[j]
        
if ans == '':
    print('PREDAJA')
else:
    print(ans)