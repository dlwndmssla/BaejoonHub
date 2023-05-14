import sys
input = sys.stdin.readline

list1 = [0]
bingo = [0]

for i in range(5):
    x = list(map(int, input().split()))
    list1 += x

for i in range(5):
    y = list(map(int, input().split()))
    bingo += y
    
row = [[ i*5+j for i in range(5)] for j in range(1,6)]
col = [[i+5*j for i in range(1,6)] for j in range(5)]
cross = [[1, 7, 13, 19, 25],[5, 9, 13, 17, 21]]
okey = row+col+cross

for i in range(1,26):
    b = bingo[i]
    idx = list1.index(b)
    for j in range(12):
        if idx in okey[j]:
            okey[j].remove(idx)
    if okey.count([]) >= 3:
        break
print(i)