class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return ceil(piles[0]/h)

        def hourCount(midd):
            count = 0
            pt = 0
            while pt < len(piles):
                count += ceil(piles[pt] / midd)
                pt += 1

            return count

        high, low = max(piles), 1
        ans = high
        while low <= high:
            mid = (low + high)//2
            result = hourCount(mid)

            if result <= h:
                ans =  mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
