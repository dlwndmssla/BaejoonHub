m = int(input())
n = int(input())
number = []

for i in range(2,n+1):
    number.append(i)

for i in range(2,n+1):
    
    for j in range(2,n):
        if i !=j:
            if i%j == 0:
                number.remove(i)
                break

exam = []
sum = 0
for i in range(len(number)):
    
    if number[i] >= m and number[i] <= n:
        exam.append(number[i])
        sum += number[i]

if len(exam) != 0:
    print(sum)
    print(exam[0])
else:
    print(-1)