mock_nums = [2, 5, 6, 11]
mock_target = 16

for i in range(len(mock_nums)):
    for j in range(i + 1, len(mock_nums)):
        if mock_nums[i] + mock_nums[j] == mock_target:
            print(i, j)
            exit()

# book 1
for i in range(len(mock_nums)):
    for j in range(i + 1, len(mock_nums)):
        if mock_nums[i] + mock_nums[j] == mock_target:
            print([i, j])
            exit()

# book 1
for i, n in enumerate(mock_nums):
    complement = mock_target - n
    if complement in mock_nums[i + 1:]:
        print([mock_nums.index(n), mock_nums[i + 1:].index(complement) + (i + 1)])
        exit()

# book 3
nums_map = {}
for i, num in enumerate(mock_nums):
    nums_map[num] = i

for i, num in enumerate(mock_nums):
    if mock_target - num in nums_map and i != nums_map[mock_target - num]:
        print([i, nums_map[mock_target - num]])
        exit()


# book 4
nums_map = {}
for i, num in enumerate(mock_nums):
    if mock_target - num in nums_map:
        print([nums_map[mock_target - num], i])
        exit()
    nums_map[num] = i
