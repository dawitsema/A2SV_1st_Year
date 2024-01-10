class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        maxx = 0
        s_set = set()
        for i in range(len(s)):
            if s[i] not in s_set:
                s_set.add(s[i])
                count += 1
                maxx = max(maxx, count)
            else:
                s_set.clear()
                count = 1
                pt = i - 1
                s_set.add(s[i])
                while s[pt] != s[i]:
                    s_set.add(s[pt])
                    count += 1
                    pt -= 1
                
        
        return maxx



        