class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)-1):
            j = i + 1
            while j < len(nums) and nums[i] + nums[j] < target:
                count += 1
                j += 1  

        return count


        