class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def helper(num):
            if num < 3 and num != 1:
                return False
            if num == 3 or num == 1:
                return True
            return helper(num/3)
        
        return helper(n)
