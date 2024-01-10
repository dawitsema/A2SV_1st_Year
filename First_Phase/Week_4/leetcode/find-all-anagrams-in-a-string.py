class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dicP = Counter(p)
        m = len(p)

        ans = []
        l=0
        for i in range(m, len(s)):
            dicS = Counter(s[l:i])
            if dicS == dicP:
                ans.append(l)
            l += 1
            
        dicS = Counter(s[l:len(s)])
        if dicS == dicP:
            ans.append(l)
        
        return ans
            
        