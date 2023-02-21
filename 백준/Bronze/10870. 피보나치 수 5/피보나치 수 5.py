m = int(input())
exam = [0]
a = 1
for i in range(1,m+1 ):
    exam.append(a)
    a = a+ exam[i-1]
print(exam[m])