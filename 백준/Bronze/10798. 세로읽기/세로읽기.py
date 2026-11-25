import sys
# input = sys.stdin.readline

arr = []
for i in range(5):
    str0 = list(input().strip())
    if len(str0) < 15:
        for i in range(15-len(str0)):
            str0.append(" ")
    arr.append(str0)
    


transposed = [list(row) for row in zip(*arr)]
result = [x for row in transposed for x in row]
print(''.join(result).replace(" ", ""))