class Solution(object):
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers) - 1
        while l < r:
            sums = numbers[l] + numbers[r]
            if sums < target:
                l += 1
            elif sums > target:
                r -= 1
            else:
                return [l+1, r+1]
        return []
        