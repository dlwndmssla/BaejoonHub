T = int(input())
score = input().split()
max_score = 0.0

for i in range(T):
    score[i] = int(score[i])
    if max_score < score[i]:
        max_score = score[i]

sum = 0   
for i in range(T):
    score[i] = float(score[i]/max_score*100)
    sum += score[i]
    
print(round(sum/T, 5))