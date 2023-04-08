import sys
input = sys.stdin.readline
n = int(input())
a = int(input())
if n != 1:
    ticket = []
    for i in range(n-1):
        ticket.append(int(input()))

    x = 0
    while a <= max(ticket):
        k = ticket.index(max(ticket))
        x += 1
        a += 1
        ticket[k] -= 1

    print(x)
else:
    print(0)