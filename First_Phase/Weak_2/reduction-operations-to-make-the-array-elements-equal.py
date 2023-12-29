class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse = True)
        
        count = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                count += i

        return count
        