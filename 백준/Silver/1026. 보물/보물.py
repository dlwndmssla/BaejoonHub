T = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

sum = 0

for i in range(T):
    sum += A[i]*B[T-1-i]
    
print(sum)