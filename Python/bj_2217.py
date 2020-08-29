# https://www.acmicpc.net/problem/2217

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
