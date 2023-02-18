exam = []
sum=0
for i in range(5):
    a = int(input())
    exam.append(a)
    sum += a
exam.sort()

print(int(sum/5))
print(exam[2])