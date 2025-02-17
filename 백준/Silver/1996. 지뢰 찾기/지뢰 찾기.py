import sys
input = sys.stdin.readline
def cnt_mines(y,x):
    if stars[y][x] in nums :return '*'
    mines = 0
    for dy in range(-1,2):
        for dx in range(-1,2):
            y1,x1 = y+dy,x+dx
            if not((n>x1>-1) and (n>y1>-1)): continue
            if not stars[y1][x1] in nums: continue
            mines += int(stars[y1][x1])
            if mines > 9:
                mines = 'M'
                return mines
    return mines

n = int(input())
nums = [str(i) for i in range(10)]
stars = [str(input()) for i in range(n)]
land_mind = [[cnt_mines(y0,x0) for x0 in range(n)] for y0 in range(n)]
for row in land_mind: print(''.join(map(str,row)))