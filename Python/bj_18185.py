# https://www.acmicpc.net/problem/18185

factory_num = input()
purchase_count = [int(x) for x in input().split()]

# 1 1 1 0 2
# 1 2 1 1 = 12
# 1 1 2 1 = 12

total = 0
idx: int = 0
while idx < len(purchase_count):
    if len(purchase_count) > idx+2 and purchase_count[idx] > 0 and purchase_count[idx+1] > 0 and purchase_count[idx+2] > 0:
        if purchase_count[idx] < purchase_count[idx+1]:
            total += 5
            purchase_count[idx] -= 1
            purchase_count[idx+1] -= 1
            continue
        if purchase_count[idx+1] > purchase_count[idx+2]:
            total += 5
            purchase_count[idx+1] -= 1
            purchase_count[idx+2] -= 1
            continue
        total += 7
        purchase_count[idx] -= 1
        purchase_count[idx+1] -= 1
        purchase_count[idx+2] -= 1
        continue
    if len(purchase_count) > idx+1 and purchase_count[idx] > 0 and purchase_count[idx+1] > 0:
        total += 5
        purchase_count[idx] -= 1
        purchase_count[idx+1] -= 1
        continue
    if len(purchase_count) > idx and purchase_count[idx] > 0:
        total += 3
        purchase_count[idx] -= 1
        continue
    idx += 1

print(total)
