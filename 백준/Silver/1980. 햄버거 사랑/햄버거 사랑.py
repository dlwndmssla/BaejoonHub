import sys
input = sys.stdin.readline
a,b,t = map(int, input().split())
bugger = []
time = []

a,b = min(a,b),max(a,b)
for i in range(int(t/a)+1):
    
    k = t-a*i
    bugger.append(i+int(k/b))
    k = k%b
    time.append(k)


time_min = min(time)
ex = []
for j in range(len(time)):
    if time[j] == time_min:
        ex.append(bugger[j])

print(max(ex), time_min)