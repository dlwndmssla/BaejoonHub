X = str(input())
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '22233344455566677778889999'
alpha_num = {i:int(j) for i,j in zip(alpha,num)}

print(sum([alpha_num[x] for x in X])+len(X))