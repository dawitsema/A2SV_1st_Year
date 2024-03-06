class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        high, low = sum(weights), max(weights)

        def dayCount(mid):
            res = 0
            count = 0
            pt = 0
            while pt < len(weights):
                res += weights[pt]
                if res > mid:
                    count += 1
                    res = 0
                    pt -= 1
                pt += 1
            return count + 1

        ans = max(weights)
        while low <= high:
            midd = (low + high) // 2

            if dayCount(midd) <= days:
                ans = midd
                high = midd - 1
            else:
                low = midd + 1

        return ans
