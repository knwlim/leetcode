from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        return c.most_common(len(nums))[-1][0]

# https://leetcode.com/problems/single-number/