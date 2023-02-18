x, y, w, h = list(map(int, input().split()))

exam = []
exam.append(x)
exam.append(y)
exam.append(w-x)
exam.append(h-y)

exam.sort()
print(exam[0])