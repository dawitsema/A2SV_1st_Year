class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)  
        minn = float("inf")

        count = 0
        for i in range(k):
            if blocks[i] == "W":
                count += 1
        minn = min(count, minn)

        for i in range(0, n-k):
            if blocks[i] == "W":
                count -= 1
            if blocks[i+k] == "W":
                count += 1
            minn = min(count, minn)

        return minn if minn != float("inf") else 0



