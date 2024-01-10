class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = maxx = zeros = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            
            if zeros < 2:
                count += 1
                maxx = max(maxx, count)
            else:
                zeros = 1
                pt = i-1
                count = 1
                while nums[pt] != 0:
                    count += 1
                    pt -= 1
        
        return maxx-1
        
                
        