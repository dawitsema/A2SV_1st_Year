class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxx = count = 0
        check = {"a", "e", "i", "o", "u"}

        for i in range(k):
            if s[i] in check:
                count += 1
        maxx = count

        for i in range(k, len(s)):
            if s[i] in check:
                count += 1
            if s[i-k] in check:
                count -= 1

            maxx = max(count, maxx)
            
        return maxx

        