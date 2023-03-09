exam = list(input())
exam.sort()
exam = exam[::-1]
a = str()
for i in range(len(exam)):
    a += str(exam[i])
print(a)