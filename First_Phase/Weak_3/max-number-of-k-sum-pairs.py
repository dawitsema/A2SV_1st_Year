class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        right = len(nums)-1
        left = 0

        count_opp = 0
        while left < right:
            if nums[left] + nums[right] == k:
                count_opp += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1

        return count_opp


        