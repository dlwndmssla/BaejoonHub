import sys
from string import ascii_lowercase
alpha = list(ascii_lowercase)
a = str(input())
b = list(set(a))
exam = [-1 for i in range(26)]
for i in range(len(b)):
    exam[alpha.index(b[i])] = a.index(b[i])

print(*exam)