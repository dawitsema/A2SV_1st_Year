
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        data = sorted((interval[0], i) for i, interval in enumerate(intervals))

        def helper(end):

            left, right = 0, len(data) - 1
            ans = float("inf")

            while left <= right:
                midd = (left + right) // 2

                if data[midd][0] >= end:
                    ans = min(ans, data[midd][1])
                    right = midd - 1
                else:
                    left = midd + 1

            return ans if ans != float("inf") else -1

        result = [helper(interval[1]) for interval in intervals]
        return result