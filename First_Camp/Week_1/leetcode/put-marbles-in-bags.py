class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        marbleSum = sorted([weights[i] + weights[i-1] for i in range(1, len(weights))])
        n = len(marbleSum)
        maxx = 0
        for i in range(n-1, n-k, -1):
            maxx += marbleSum[i]

        minn = 0
        for i in range(k-1):
            minn += marbleSum[i]
        
        return maxx - minn

        
