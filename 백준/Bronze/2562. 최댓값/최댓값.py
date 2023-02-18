max = 0

for i in range(9):
    a = int(input())
    if a > max:
        max = a
        k = i+1
    if i == 8:
        print(max)
        print(k)