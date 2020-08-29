# https://www.acmicpc.net/problem/1969

import sys

dic = {"A": 0, "T": 0, "G": 0, "C": 0}
a, b = sys.stdin.readline().split()
lists = []
for _ in range(int(a)):
    c = sys.stdin.readline()
    lists.append(c)

for bidx in range(int(b)):
    for aidx in range(int(a)):
        if lists[aidx][bidx] == "A":
            dic["A"] += dic["A"]
        elif lists[aidx][bidx] == "T":
            dic["T"] += dic["T"]
        elif lists[aidx][bidx] == "G":
            dic["G"] += dic["G"]
        elif lists[aidx][bidx] == "C":
            dic["C"] += dic["C"]
        