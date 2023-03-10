a = 1
for i in range(3):
    a = a*int(input())
b = str(a)
for i in range(10):
    print(b.count(str(i)))