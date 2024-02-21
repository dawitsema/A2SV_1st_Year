class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        nums.reverse()
        count = 0
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                temp = ceil(nums[i]/nums[i-1]) 
                count += temp - 1
                nums[i] = nums[i]//temp
        return count
        
        