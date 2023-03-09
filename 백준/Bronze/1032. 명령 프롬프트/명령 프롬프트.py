T = int(input())
exam = []
for i in range(T):
    exam.append(str(input()))

exam2 = str()
for i in range(len(exam[0])):
    a = {exam[j][i] for j in range(T)}
    a = list(a)
    if len(a) == 1:
        exam2 += str(a[0])
    else:
        exam2 += str('?')
        
print(exam2)