import itertools
import sys
input = sys.stdin.readline

def count_space(list0):
    for y in range(n):
        for x in range(1,n):
            if list0[y][x]:
                list0[y][x] += list0[y][x-1]
                
    return sum(list0,[]).count(2)


n = int(input())
room = [str(input()) for i in range(n)]
room_space = [[int(r[i]=='.') for i in range(n)] for r in room]

room_space_r = room_space
room_space_c = list(list(i) for i in zip(*room_space))

print(count_space(room_space_r),count_space(room_space_c))