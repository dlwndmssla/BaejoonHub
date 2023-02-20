N,M = map(int, input().split())

mini = min(N,M)
exam = []

for i in range(N):
    list1 = list(map(str, input().split()))
    exam.append(list1)
k = 1
sum = []

if mini != 1:

    while k < mini :
        for i in range(N - k):
            
            for j in range(M -k):

                if int(exam[i][0][j]) == int(exam[i][0][j+k]) == int(exam[i+k][0][j]) == int(exam[i+k][0][j+k]):
                    sum.append(k)
        
        k += 1
        
    if len(sum) == 0:
        print(1)
    else:
        print(pow((max(sum)+1),2))

else:
    print(1)