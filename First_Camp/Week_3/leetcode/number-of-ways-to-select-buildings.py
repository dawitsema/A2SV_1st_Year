class Solution:
    def numberOfWays(self, s: str) -> int:
        one = zero = ans = 0
        zeros = [0]*(len(s) + 1)
        once = [0]*(len(s) + 1)
        for i in range(len(s)):
            if s[i] == "0":
                zero += 1
                zeros[i+1] = one
            else:
                one += 1
                once[i+1] = zero

            zeros[i+1] += zeros[i]
            once[i+1] += once[i]

        for i in range(len(s)):
            if s[i] == "0":
                ans += once[i]
            else:
                ans += zeros[i]

        return ans
