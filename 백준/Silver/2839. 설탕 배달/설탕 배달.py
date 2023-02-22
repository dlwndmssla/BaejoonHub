m = int(input())
n = int(m/5)
exam = []
for i in range(n+1):
    k = m - 5*i
    h = k/3
    if h == int(h):
        exam.append(i+h)
if len(exam) != 0:
    print(int(min(exam)))
else:
    print(-1)