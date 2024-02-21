class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        nums.sort(reverse=True)
        n = len(nums)
        for i in range(n-2):
            left = i + 1
            right = n - 1
            while left < right:
                if nums[i] < nums[left] + nums[right]:
                    count += right - left
                    left += 1
                else:
                    right -= 1
        
        return count


        