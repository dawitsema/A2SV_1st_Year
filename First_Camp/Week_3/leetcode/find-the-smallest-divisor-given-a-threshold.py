class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def helper(div):
            summ = 0
            for i in range(len(nums)):
                summ += ceil(nums[i] / div)

            return summ

        left, right = 1, max(nums)
        ans = right


        while left <= right:
            midd = (left + right) // 2
            result = helper(midd)

            if threshold < result:
                left = midd + 1
            else:
                ans = min(midd, ans)
                right = midd - 1
                

        return ans
