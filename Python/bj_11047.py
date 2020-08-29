# https://www.acmicpc.net/problem/11047

import sys

count = 0
values = []

a = sys.stdin.readline().split()

price = int(a[1])

for idx in range(int(a[0])):
    values.append(int(sys.stdin.readline()))

values.reverse()

for val in values:
    if val > price:
        continue
    if price != 0:
        subCount = int(price / val)
        count += subCount
        price -= subCount * val
    else:
        break

print(count)