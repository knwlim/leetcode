# Time Limit Exceeded
class Recursive_Solution:
    def climbStairs(self, n: int) -> int:
        """
        F(10)=F(9)+F(8);
        F(9)=F(8)+F(7);
        F(8)=F(7)+F(6);
        ...
        F(2) = 2
        F(1) = 1
        """
        if n == 1: return 1
        if n == 2: return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

# dynamic programming
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        step_1, step_2 = 1, 2
        for _ in range(2, n):
            step_1, step_2 = step_2, step_1 + step_2
        return step_2

# https://leetcode.com/problems/climbing-stairs/
