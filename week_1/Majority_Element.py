class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s, max, answer = set(nums), 0, 0
        for item in s:
            count = nums.count(item)
            if count > max:
                answer = item
                max = count
        return answer
    
# https://leetcode.com/problems/majority-element/
