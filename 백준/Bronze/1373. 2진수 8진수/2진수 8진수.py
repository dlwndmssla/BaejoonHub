import sys
#input = sys.stdin.readline
T = list(input())
T = T[::-1]
M = [1,2,4]
b = str()
c = 0
for i in range(len(T)):
    c += int(T[i])*M[i%3]
    if i%3 ==2 :
        b += str(c)
        c = 0
    elif i == len(T) -1:
        b += str(c)
    
print(b[::-1])