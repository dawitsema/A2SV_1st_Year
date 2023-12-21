class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        n1, n2 = float("inf"), float("inf")

        for i in range(len(nums)):
            if nums[i] > n2:
                return True
            
            if n1 < nums[i] and nums[i] < n2:
                n2 = nums[i]
            else:
                n1 = min(n1, nums[i])


        return False

        
                
         