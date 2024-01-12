class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        summ = maxx = nums[0]
        right = 1
        left = 0
        check = {nums[0]}
        while right < len(nums):
            if nums[right] not in check:
                summ += nums[right]
                check.add(nums[right])
                right += 1
            else:
                while nums[left] != nums[right]:
                    check.remove(nums[left])
                    summ -= nums[left]
                    left += 1
                check.remove(nums[left])
                summ -= nums[left]
                left += 1
            
            maxx = max(summ, maxx)

        return maxx

            

            