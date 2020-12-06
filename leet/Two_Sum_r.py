mock_nums = [2, 5, 5, 11]
mock_target = 10

for i in range(len(mock_nums)):
    for j in range(i + 1, len(mock_nums)):
        if mock_nums[i] + mock_nums[j] == mock_target:
            print(i, j)

