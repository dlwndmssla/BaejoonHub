T = int(input())
exam = list(map(int, input().split()))
exam.sort()
sum= 0 
exam2 = []
for i in range(T):
    sum += exam[i]
    exam2.append(sum)
sum2 = 0
for i in range(T):
    sum2 += exam2[i]
    
print(sum2)