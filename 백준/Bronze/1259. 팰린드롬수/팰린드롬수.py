import sys
#input = sys.stdin.readline
while 1:
    a = str(input())
    if a == str(0):
        break
    b = str(int(a[::-1]))
    if a !=b:
        print('no')
    else:
        print('yes')