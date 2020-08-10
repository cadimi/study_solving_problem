# https://www.acmicpc.net/problem/11399

input()
total = 0
alist = sorted(list(map(int, input().split(" "))))
for x, y in enumerate(alist):
    total += y
    while x != 0:
        x -= 1
        total += alist[x]
print(total)
