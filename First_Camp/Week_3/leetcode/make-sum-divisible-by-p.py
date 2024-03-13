class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        r = sum(nums) % p
        
        if r == 0:
            return 0
        
        prefix_sum = {0: -1}  #
        temp_r = 0
        min_length = float('inf')
        
        for i, num in enumerate(nums):
            temp_r = (temp_r + num) % p
            prefix_sum[temp_r] = i
            
            complement_remainder = (temp_r - r) % p
            if complement_remainder in prefix_sum:
                min_length = min(min_length, i - prefix_sum[complement_remainder])
        
        return min_length if min_length != float('inf') and min_length != len(nums) else -1
            