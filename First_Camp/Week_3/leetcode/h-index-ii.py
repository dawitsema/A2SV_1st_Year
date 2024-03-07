class Solution:
    def hIndex(self, citations: List[int]) -> int:

        left, right = 0, len(citations) - 1
        ans = left
        while left <= right:

            midd = (left + right) // 2
            if citations[midd] >= len(citations) - midd:
                ans = len(citations) - midd
                right = midd - 1
            else:
                left = midd + 1

        return ans
