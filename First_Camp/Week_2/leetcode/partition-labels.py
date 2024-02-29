class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic1 = defaultdict(int)
        for i in range(len(s)):
            if s[i] not in dic1:
                dic1[s[i]] = i
            else:
                dic1[s[i]] = i
        
        ans = []
        ref = dic1[s[0]]
        check = 0
        for i in range(len(s)):
            if ref <= dic1[s[i]]:
                ref = dic1[s[i]]
            if dic1[s[i]] == i and dic1[s[i]] == ref:
                temp = ref + 1 - check
                check += temp
                ans.append(temp)
            

        return ans
            
        