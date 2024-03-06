class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            midd = (low + high)//2
            if nums[midd] == target:
                return midd
            elif nums[midd] > target:
                high = midd - 1
            else:
                low = midd + 1

        return low