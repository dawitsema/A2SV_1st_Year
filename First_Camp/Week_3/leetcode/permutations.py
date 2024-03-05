class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        hashset = set()

        def helper(start, temp):
            if len(temp) == len(nums):
                set1 = set(temp.copy())
                if len(temp.copy()) == len(set1):
                    ans.append(temp.copy())
                return
            for i in range(len(nums)):
                temp.append(nums[i])
                helper(start + 1, temp)
                temp.pop()

        helper(0, [])
        return ans
