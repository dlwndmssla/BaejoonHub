num = list(map(int,input().split()))
print(min(min(num[0],num[0+2]-num[0]),min(num[1],num[1+2]-num[1])))
