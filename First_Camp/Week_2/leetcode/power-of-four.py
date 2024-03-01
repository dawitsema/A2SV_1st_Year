class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def helper(num):
            if num < 4 and num != 1:
                return False
            if num == 4 or num == 1:
                return True
            return helper(num/4)
        
        return helper(n)
