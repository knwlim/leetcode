# O(n^3) Solution -> Time Limit Exceeded
class n3_Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        for left in range(len(nums)):
            window_sum = 0
            for right in range(left, len(nums)):
                window_sum = sum(nums[left:right+1])
                max_sum = max(window_sum, max_sum)
        return max_sum

# O(n^2) Solution -> Time Limit Exceeded
class n2_Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        for left in range(len(nums)):
            window_sum = 0
            for right in range(left, len(nums)):
                window_sum += nums[right]
                max_sum = max(window_sum, max_sum)
        return max_sum

# O(n) Solution - dynamic programming
"""
as iterating over the array from 0, find the maximum sum we've achived so far 
when current element is bigger than the sum(including current element) we've achived so far, 
it's better to start the subarray from current element.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum_so_far = sum_so_far = -float('inf')
        for i in range(len(nums)):
            sum_so_far += nums[i]
            sum_so_far = max(sum_so_far, nums[i]) 
            max_sum_so_far = max(max_sum_so_far, sum_so_far)
        return max_sum_so_far