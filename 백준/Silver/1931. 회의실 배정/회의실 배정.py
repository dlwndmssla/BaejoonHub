import sys
input = sys.stdin.readline
n = int(input())
 
time= sorted([list(map(int,input().split())) for i in range(n)], key=lambda x: (x[1], x[0]))
meetings = [time[0]]
for i in range(1,n):
    if meetings[-1][1]<= time[i][0]:
        meetings.append(time[i])

print(len(meetings))