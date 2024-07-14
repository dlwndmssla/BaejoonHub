n = int(input())

time = list(map(int,input().split()))
timed = sorted(time)
print(sum([ timed[i]*(n-i) for i in range(n)]))