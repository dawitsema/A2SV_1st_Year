class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_Nums = sorted(nums)
        dic = {}
        ans = []

        for i in range(len(sorted_Nums)):
            if sorted_Nums[i] not in dic:
                dic[sorted_Nums[i]] = i

        for i in range(len(nums)):
            ans.append(dic[nums[i]])
        
        return ans



        