import sys
input = sys.stdin.readline
n = int(input())
ex1 = ['x']
ex1 += list(map(int, input().split()))
student = ['x']
switch = ['x']
s = int(input())
for i in range(s):
    a,b = map(int, input().split())
    student.append(a)
    switch.append(b)
    
for i in range(1,s+1):
    d = switch[i]
    if student[i] ==1:
        for j in range(d,len(ex1), d):
            ex1[j] = abs(ex1[j]-1)
    else:
        for k in range(d,0,-1):
            if 2*d-k < len(ex1):
                if ex1[k] == ex1[2*d-k]:
                    ex1[k] = ex1[2*d-k] = abs(ex1[k]-1)
                else:
                    break

for i in range(1,len(ex1),20):
    print(*ex1[i:i+20])