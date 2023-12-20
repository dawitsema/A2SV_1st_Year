class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        count = 0
        ans = [''.join(st[i] for st in strs) for i in range(len(strs[0]))]

        for i in range(len(ans)):
            for j in range(len(ans[0])-1):
                if ans[i][j] > ans[i][j+1]:
                    count += 1
                    break

        return count

       
        return count


        

        