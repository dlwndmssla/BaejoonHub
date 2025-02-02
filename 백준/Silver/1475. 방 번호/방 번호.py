import math
room = str(input())
counts = [0 for i in range(9)]
for i in room:
    if i == '9':
        counts[6] += 1
    else:
        counts[int(i)] += 1

counts[6] = math.ceil(counts[6]/2)

print(max(counts))