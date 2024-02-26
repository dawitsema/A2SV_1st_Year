class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        frequency = [0] * len(nums)
        for req in requests:
            frequency[req[0]] += 1
            if req[1] + 1 < len(frequency):
                frequency[req[1] + 1] -= 1
        prefix = [0]
        for i in range(len(frequency)):
            prefix.append(prefix[-1] + frequency[i])

        prefix.sort(reverse=True)
        nums.sort(reverse=True)
        print(prefix, nums)
        
        ans = 0
        for i in range(len(nums)):
            ans += prefix[i] * nums[i]

        return ans%(10**9 + 7)
