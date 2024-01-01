class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        res = []

        def sort(cakes, n):
            if n == 1:
                return
            max_cake = 0
            max_cake_index = 0

            for i in range(n):
                if cakes[i] > max_cake:
                    max_cake_index = i
                    max_cake = cakes[i]

            reverse(cakes, 0, max_cake_index)
            res.append(max_cake_index+1)

            reverse(cakes, 0, n-1)
            res.append(n)

            sort(cakes, n-1)

        def reverse(arr, i, j):
            while i< j:
                arr[i], arr[j]= arr[j], arr[i]
                i+=1
                j-=1

        sort(arr, len(arr))
        return res