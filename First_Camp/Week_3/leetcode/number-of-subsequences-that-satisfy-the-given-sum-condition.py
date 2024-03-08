class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        MOD = (10**9) + 7
        ans = 0
        right = len(nums) - 1

        for i in range(len(nums)):

            left = i
            count = 0
            
            while left <= right:
                midd = (left + right)//2
                temp = nums[i] + nums[midd]
                if temp > target:
                    right = midd - 1
                    
                else:
                    left = midd + 1
                    count = pow(2, midd - i, MOD)

            if count:
                ans += count % MOD
            else:
                break
           
        
        return ans % MOD
