# https://www.acmicpc.net/problem/1138
import sys

a = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
r = [0]*a

for idx in range(1, a+1):
    val = b[idx-1]
    count = 0
    for i in range(a):
        if count == val and r[i] == 0:
            r[i] = val
            break
        elif r[i] == 0:
            count += 1

print(*r, sep=" ")
