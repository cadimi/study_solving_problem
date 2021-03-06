"""
https://leetcode.com/problems/product-of-array-except-self/

Input:  [1,2,3,4]
Output: [24,12,8,6]
"""

nums = [2, 3, 4, 5]

# self, not O(n)
output = []
one = 1
for i in range(0, len(nums)):
    for j, vt in enumerate(nums):
        if i == j:
            continue
        one = one * vt
    output.append(one)
    one = 1
print(output)

# # solution book
out = []
p = 1

for i in range(0, len(nums)):  # 0 ~ 4
    out.append(p)
    p = p * nums[i]
p = 1

for i in range(len(nums) - 1, 0 - 1, -1):  # 3 ~ -1
    out[i] = out[i] * p
    p = p * nums[i]
print(out)
