N = int(input())
exam = list(map(int, input().split()))
exam.sort()
M = max(exam)
sum = 0   
for i in exam:
    exam1 = []
    if i == 2:
        sum += 1
    elif i >2 and i%2 !=0:
        for j in range(3, int(i/2)+1):
            if i != j and i%j == 0:
                exam1.append(j)
        if len(exam1) == 0:
            sum += 1
print(sum)