class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        run_sum = 0
        maxx = 0

        for num in nums:
            run_sum += num
            if run_sum < 0:
                run_sum = 0
            maxx = max(run_sum, maxx)
        
        return maxx if maxx else max(nums)