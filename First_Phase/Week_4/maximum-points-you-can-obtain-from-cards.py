class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        summ = maxx = 0

        summ = sum(cardPoints[:-(k+1):-1])
        maxx = summ
        for i in range(n-k,n):
            summ -= cardPoints[i%n]
            summ += cardPoints[(i+k)%n]

            maxx = max(maxx, summ)

        return maxx