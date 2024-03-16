class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1]*n
        for i in range(n):
            count = 0
            temp = i + 1
            while count < n:
                if nums[i] < nums[temp%n]:
                    ans[i] = nums[temp%n]
                    break
                count += 1
                temp += 1
        
        return ans