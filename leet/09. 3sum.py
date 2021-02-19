"""
https://leetcode.com/problems/3sum/

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

"""

nums = [-1, 0, 1, 2, -1, -4]

# solution 1 brute force
results = []
nums.sort()
print(nums)
for i in range(len(nums) - 2):  # 0 4
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    for j in range(i + 1, len(nums) - 1):  # 1 5
        if j > i + 1 and nums[j] == nums[j - 1]:
            continue
        for k in range(j + 1, len(nums)):  # 2 6
            if k > j + 1 and nums[k] == nums[k - 1]:
                continue
            if nums[i] + nums[j] + nums[k] == 0:
                results.append((nums[i], nums[j], nums[k]))

print(results)

# solution 2 two pointer sum
results = []
nums.sort()

for i in range(len(nums) - 2):  # 0 4
    # 중복된 값 건너뛰기
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    print("i is ", i)
    # 간격을 좁혀가며 합 `sum` 계산
    left, right = i + 1, len(nums) - 1
    while left < right:
        print("left is ", left, "right is", right)
        sum = nums[i] + nums[left] + nums[right]
        if sum < 0:
            left += 1
        elif sum > 0:
            right -= 1
        else:
            print("in")
            # `sum = 0`인 경우이므로 정답 및 스킵 처리
            results.append([nums[i], nums[left], nums[right]])

            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
            left += 1
            right -= 1

print(results)
