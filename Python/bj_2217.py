# https://www.acmicpc.net/problem/2217
# note: use max, min instead of if
# setting sys.stdin.readline() to var might be helpful (?)

import sys

a = int(sys.stdin.readline())
val = []
for _ in range(a):
    val.append(int(sys.stdin.readline()))

val.sort(reverse=True)
minc = 0
for idx, elmn in enumerate(val):
    temp = (idx + 1) * elmn
    if minc < temp:
        minc = temp

print(minc)
