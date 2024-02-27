class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]
        for i in range(n):
            prefix.append(prefix[-1] + nums[i])

        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i]

        ans = []
        for i in range(n):
            temp = (nums[i] * i - prefix[i]) + (suffix[i + 1] - nums[i]*(n-i-1))
            ans.append(temp)

        return ans
