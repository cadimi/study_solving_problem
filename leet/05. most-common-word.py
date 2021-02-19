"""
Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

Output: "ball"
"""
import collections
import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(collections.Counter([word for word in re.sub('[^a-zA-z]', ' ', paragraph).lower().split() if word not in banned]).most_common(1)[0][0])
