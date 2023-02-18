N = int(input())
exam = 1

if N !=0 :
    for i in range(1,N+1):
        exam = exam*i
    print(exam)    
else:
    print(1)