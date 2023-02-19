k = 0

for i in range(8):
    a = str(input())
    b = i%2
    for j in range(b,8,2):
        if a[j] == "F":
            k +=1

print(k)