"""
Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

# two pointer

s = ["h", "e", "l", "l", "o"]

left, right = 0, len(s) - 1
while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1

# slice

s = ["h", "e", "l", "l", "o"]
print(s[::-1])

# pythoic way

s = ["h", "e", "l", "l", "o"]
s.reverse()
print(s)