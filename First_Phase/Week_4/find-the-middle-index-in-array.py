class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:

        fromLeft = [0, nums[0]]
        for i in range(1, len(nums)):
            fromLeft.append(fromLeft[-1] + nums[i])
        fromLeft.append(fromLeft[-1])
        
        fromRight = [0, nums[-1]]
        for i in range(len(nums)-2, -1, -1):
            fromRight.append(fromRight[-1] + nums[i])
        fromRight.append(fromRight[-1])

        indx = - 1
        n = len(fromLeft)
        for i in range(1,n-1):
            if fromRight[i] == fromLeft[n-i-1]:
                indx = n - i - 2


        return indx

        