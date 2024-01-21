class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic1 = {0:1}
        pre_sum = 0
        count = 0

        for num in nums:
            pre_sum += num
            temp = pre_sum % k
            if temp in dic1:
               count += dic1[temp] 
               dic1[temp] += 1
            else:
                dic1[temp] = 1

        return count 

        
        