T = int(input())

exam = []
for i in range(T):
    a = int(input())
    exam.append(a)
    
exam.sort()

for i in range(T):
    print(exam[i])