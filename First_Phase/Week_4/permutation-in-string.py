class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dic = Counter(s1)
        m = len(s1)
        l = 0

        for i in range(m, len(s2)+1):
            s2_dic = Counter(s2[l:i])
            if s1_dic == s2_dic:
                return True
            l += 1

        return False

        