import sys
input=sys.stdin.readline
n = int(input())
age = []
name = []
for i in range(n):
    a,b = map(str, input().split())
    a = int(a)
    age.append(a)
    name.append(b)
set_age = set(age)
for i in set_age:
    ex1 = []
    for j in range(n):
        if (i == age[j]):
            ex1.append(name[j])
    for k in range(len(ex1)):
        print(i,ex1[k])