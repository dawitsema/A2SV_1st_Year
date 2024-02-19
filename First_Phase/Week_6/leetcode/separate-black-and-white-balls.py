class Solution:
    def minimumSteps(self, s: str) -> int:
        if len(s) == 1:
            return 0

        nums = []
        for st in s:
            nums.append(int(st))
        
        swaps = 0
        left = 0
        for right in range(1, len(s)):
            if nums[right] == 0:
                if nums[left] != 0:
                    swaps += right - left
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                else:
                    pass
            else:
                if nums[left] == 0:
                    left += right
        
        return swaps

        
        