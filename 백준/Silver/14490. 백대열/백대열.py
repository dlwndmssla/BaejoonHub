import sys
input = sys.stdin.readline
x = str(input())
idx = x.index(':')
a = int(x[:idx])
b = int(x[idx+1:])
k = min(a,b)
num = [k]
for i in range(1,int(k/2)+1):
    if k%i == 0:
        num.append(i)
num.sort()
num = num[::-1]
for i in num:
    if a%i == b%i == 0:
        ans = str(int(a/i))+':'+ str(int(b/i))
        print(ans)
        break