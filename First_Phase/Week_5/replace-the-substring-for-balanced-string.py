class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        target = n // 4
        
        char_count = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        for char in s:
            char_count[char] += 1
        
        def is_balanced():
            return all(count <= target for count in char_count.values())
        
        if is_balanced():
            return 0
        
        i, res = 0, n
        for j in range(n):
            char_count[s[j]] -= 1
            
            while is_balanced():
                res = min(res, j - i + 1)
                char_count[s[i]] += 1
                i += 1
        
        return res
