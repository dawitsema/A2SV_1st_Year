class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = odd_count = subarray_count = result = 0

        for right in range(n):
            if nums[right] & 1:
                odd_count += 1
                subarray_count = 0
            while odd_count == k:
                subarray_count += 1
                if nums[left] & 1:
                    odd_count -= 1
                left += 1
            result += subarray_count
        return result
