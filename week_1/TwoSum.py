class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        saved = {}
        for idx, val in enumerate(nums):
            if target-val in saved:
                return [idx, saved[target-val]]
            saved[val] = idx
        