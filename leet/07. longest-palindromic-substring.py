"""
https://leetcode.com/problems/longest-palindromic-substring/

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
"""

s = "babad"


def expand(left: int, right: int) -> str:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    print(f'{left} , {right}, {s[left + 1:right]}')
    return s[left + 1:right]


if len(s) < 2 or s == s[::-1]:
    print("Exit")

result = ""
for i in range(len(s) - 1):
    result = max(result, expand(i, i+1), expand(i, i+2), key=len)

print(result)
