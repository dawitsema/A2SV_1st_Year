class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        idx_dic = {}
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if (i, j) not in idx_dic:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                    idx_dic[(i, j)] = 1
                    idx_dic[(j, i)] = 1
        
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]

        return matrix