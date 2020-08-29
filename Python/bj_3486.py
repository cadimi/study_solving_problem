# https://www.acmicpc.net/problem/3486

num = int(input())
lists = []
for index in range(num):
    sub = list(map(str, input().split(" ")))
    lists.append(int(str(int(sub[0][::-1])+int(sub[1][::-1]))[::-1]))


for idx in lists:
    print(idx)


# import sys
# r=""
# for _ in range(int(sys.stdin.readline())):
#     a, b = sys.stdin.readline().split()
#     r += str(int(str(int(a[::-1])+int(b[::-1]))[::-1]))+'\n'
# print(r, end="")