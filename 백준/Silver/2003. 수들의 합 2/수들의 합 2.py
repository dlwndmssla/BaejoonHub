import sys
input=sys.stdin.readline
a,b = map(int, input().split())
ex1 = list(map(int, input().split()))

sum_list = [0]*(a+1)
k = 0
for i in range(a):
    k += ex1[i]
    sum_list[i+1] = k

num = 0
for i in range(1,a+1):
    for j in range(i):
        x = sum_list[i]-sum_list[j]
        if b == x:
            num += 1
            
print(num)