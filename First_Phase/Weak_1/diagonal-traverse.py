class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row, col = len(mat), len(mat[0])
        arr_dic = {}

        for i in range(row):
            for j in range(col):
                if i + j not in arr_dic:
                    arr_dic[i+j] = [mat[i][j]]
                else:
                    arr_dic[i+j].append(mat[i][j])

        ans = []
        for key, val in arr_dic.items():
            if key%2 == 0:
                for x in val[::-1]:
                    ans.append(x)
            else:
                for x in val:
                    ans.append(x)
        
        return ans

            
        
        

        