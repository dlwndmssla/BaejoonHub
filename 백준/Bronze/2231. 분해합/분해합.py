#백준 1064번

n = str(input())

for i in range(int(n)+1):
    if i+sum([int(str(i)[j]) for j in range(len(str(i)))]) == int(n):
        break

if int(n) != i:
    print(i)
else:
    print(0)