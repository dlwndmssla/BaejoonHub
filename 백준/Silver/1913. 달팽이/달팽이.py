n,m = int(input()),int(input())
ans = []

nums = [[ 0 for i in range(n)] for i in range(n)]
turn_points = [1 for i in range(n*2)]
add_value = sum([[i,i] for i in range(1,n+1)],[])
for j in range(len(turn_points)-1):
    turn_points[j+1] = turn_points[j] + add_value[j] 
# print(add_value )
# print(turn_points)


x,y = int(n/2),int(n/2)

for t,i in enumerate(turn_points[:-1]):
    # print(i,t,t%4,[[-1,0],[0,1],[1,0],[0,-1]][t%4])
    for num in range(i,turn_points[t+1]):
        # print(num,"|",y,x,)
        nums[y][x] = num
        if num == m: ans = [y+1,x+1]
        dy,dx = [[-1,0],[0,1],[1,0],[0,-1]][t%4]
        x += dx
        y += dy
        
for k in nums:
    print(*k)
print(*ans)