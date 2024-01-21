class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        total = 1
        
        if 0 in nums:
            ind = nums.index(0)
            nums.remove(0)
            for i in range(len(nums)):
                total *= nums[i]
            ans[ind] = total

        else:
            for i in range(len(nums)):
                total *= nums[i]

            for i in range(len(nums)):
                ans[i] = total//nums[i]

        return ans
        