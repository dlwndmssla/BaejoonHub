ex = ['D', 'C', 'B', 'A', 'E']

for i in range(3):
    num = list(map(int, input().split()))
    a = sum(num)
    print(ex[a])