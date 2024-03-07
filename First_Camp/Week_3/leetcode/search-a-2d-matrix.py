class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        ans = right

        while left <= right:
            midd = (left + right) // 2
            print(matrix[midd][0])
            if target >= matrix[midd][0]:
                ans = midd
                left = midd + 1
            else:
                right = midd - 1

        print(ans)
        left, right = 0, len(matrix[ans]) - 1
        result = False

        while left <= right:
            midd = (left + right) // 2
            if target == matrix[ans][midd]:
                result = True
                break
            elif target < matrix[ans][midd]:
                right = midd - 1
            else:
                left = midd + 1

        return result
