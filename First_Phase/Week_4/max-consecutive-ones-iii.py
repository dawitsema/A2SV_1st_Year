
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxx = count = zeros = 0
        pt = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1

            while zeros > k:
                if nums[pt] == 0:
                    zeros -= 1
                count -= 1
                pt += 1

            count += 1
            maxx = max(count, maxx)

        return maxx

