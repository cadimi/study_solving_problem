mock_nums = [2, 5, 5, 11]
mock_target = 10

for enum, i in enumerate(mock_nums):
    for enum2, j in enumerate(mock_nums):
        if enum2+1 < len(mock_nums):
            if enum == enum2+1:
                continue
            if mock_nums[enum] + mock_nums[enum2+1] == mock_target:
                # print(f'[{enum},{enum2+1}]')
                print(enum, enum2+1)
                exit()