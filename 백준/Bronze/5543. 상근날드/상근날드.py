import sys
input = sys.stdin.readline
ex1 = []
for i in range(5):
    ex1.append(int(input()))
    
ex2 = []
for j in range(3):
    ex2.append(ex1[j]+ex1[3])
    ex2.append(ex1[j]+ex1[4])
    
print(min(ex2)-50)