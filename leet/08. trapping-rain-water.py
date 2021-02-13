"""
https://leetcode.com/problems/trapping-rain-water/

Input: height = [4,2,0,3,2,5]
Output: 9

"""
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# height = [0, 1, 0, 3, 1, 0, 1, 2, 2, 1, 2, 1]
# height = [0, 1, 0, 3, 1, 0, 1, 3, 2, 1, 2, 1]

# solution 1
if not height:
    exit()

volume = 0
left, right = 0, len(height) - 1
left_max, right_max = height[left], height[right]

while left < right:
    left_max, right_max = max(height[left], left_max), \
                          max(height[right], right_max)
    if left_max <= right_max:
        volume += left_max - height[left]
        left += 1
    else:
        volume += right_max - height[right]
        right -= 1
    print(volume, left_max, right_max, left, right)

print(volume)

# solution 2
stack = []
volume = 0
for i in range(len(height)):
    while stack and height[i] > height[stack[-1]]:
        print("i: ", i, ", stack: ", stack)
        top = stack.pop()
        if not len(stack):
            break

        distance = i - stack[-1] - 1
        waters = min(height[i], height[stack[-1]] - height[top])

        volume += distance * waters
        print("distance: ", distance, ", waters: ", waters, ", volume: ", volume)
    stack.append(i)

print(volume)
