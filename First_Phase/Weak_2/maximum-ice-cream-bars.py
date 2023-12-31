class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

            def count_sort(arr):
                mmin, mmax = min(arr),max(arr)
                k = mmax - mmin + 1

                counts = [0]*k
                for nm in arr:
                    counts[nm-mmin] += 1

                indx = 0
                for i in range(k):
                    for j in range(counts[i]):
                        arr[indx] = i + mmin
                        indx += 1
                
                return arr
        
            costs = count_sort(costs)
            count = 0
            for i in range(len(costs)):
                if coins - costs[i] >= 0:
                    count += 1
                    coins -= costs[i]
                else:
                    break
            
            return count






        