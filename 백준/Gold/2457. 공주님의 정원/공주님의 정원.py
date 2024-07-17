import sys
input = sys.stdin.readline
n = int(input())
f = [list(map(int, input().split())) for i in range(n)]
flower = sorted([[f[i][0]*100+f[i][1],f[i][2]*100+f[i][3]]for i in range(n)])

cnt = 0
end_time = 301

while flower:
    if (end_time >= 1201) or (flower[0][0] > end_time): break
    check_end_date = -1
    for i in range(len(flower)):
        if flower[0][0] <= end_time:
            if check_end_date <= flower[0][1]:
                check_end_date = flower[0][1]
            flower.remove(flower[0])
        else: break
    end_time = check_end_date
    cnt += 1

if end_time < 1201:
    print(0)
else:
    print(cnt)