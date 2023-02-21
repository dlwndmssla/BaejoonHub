t = int(input())
for i in range(t):
    a,b = map(int, input().split())
    exam = [a]
    for i in range(2, int(a/2)+1):
        if a%i == 0:
            exam.append(i)
    exam1 = [1]
    for j in range(len(exam)):
        if b%exam[j] == 0:
            exam1.append(exam[j]) 
    c = max(exam1)
    print(int(a*b/c))   