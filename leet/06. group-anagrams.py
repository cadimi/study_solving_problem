"""
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""
import collections

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagrams = collections.defaultdict(list)

for word in strs:
    anagrams[''.join(sorted(word))].append(word)

print(list(anagrams.values()))

# sorted returns list