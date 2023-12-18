class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i, j = 0, k
        ans = ""
        count = 0
        while i < len(s):
            if j < len(s):
                if count%2 == 0:
                    ans += s[i:j][::-1]
                else:
                    ans += s[i:j]
            else:
                if count%2 == 0:
                    ans += s[i:][::-1]
                else:
                    ans += s[i:]

            i += k
            j += k
            count += 1

        return ans


