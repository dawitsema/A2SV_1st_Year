class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        summ = 0
        left = right = 0
        n = len(nums)
        
        minn = float("inf")
        while right < n:
            summ += nums[right]
            while summ >= target:
                minn = min(right - left + 1, minn)
                summ -= nums[left]
                left += 1

            right += 1

        return 0 if minn == float("inf") else minn
            


            
            
 