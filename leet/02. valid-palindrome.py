"""
https://leetcode.com/problems/valid-palindrome

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

# 1. deque

import collections
from typing import Deque

s = "A man, a plan, a canal: Panama"
strs: Deque = collections.deque()

for char in s:
    if char.isalnum():
        strs.append(char.lower())

while len(strs) > 1:
    if strs.popleft() != strs.pop():
        print("False")

# 2. list

s = "A man, a plan, a canal: Panama"
strs = []
for char in s:
    if char.isalnum():
        strs.append(char.lower())

while len(strs) > 1:
    if strs.pop(0) != strs.pop():
        print("False")

# 3. slice *

import re

s = "A man, a plan, a canal: Panama"
s = s.lower()
s = re.sub('[^a-z0-9]', '', s)

print(s == s[::-1])
