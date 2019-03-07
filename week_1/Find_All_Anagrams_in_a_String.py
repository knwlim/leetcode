# anagram should have the same length as p
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = list()
        num_of_each_char = Counter(p)
        for i in range(len(s) - len(p) + 1):
            if Counter(s[i : i + len(p)]) == num_of_each_char:
                result.append(i)
        return result

# https://leetcode.com/problems/find-all-anagrams-in-a-string/
