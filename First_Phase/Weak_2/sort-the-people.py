class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashmap = dict()
        hashmap = {heights[i]:names[i] for i in range(len(names))}
        n = len(heights)
        for i in range(n):
            minInd = i
            for j in range(i+1, n):
                if heights[minInd] < heights[j]:
                    minInd = j

            if minInd != i:
                heights[i], heights[minInd] = heights[minInd], heights[i]
                names[i], names[minInd] = names[minInd], names[i]

                
        # for i in range(len(heights)):
        #     for j in range(len(heights)-1-i):
        #         if heights[j] < heights[j+1]:
        #             heights[j+1], heights[j] = heights[j], heights[j+1]
        #             names[j+1], names[j] = names[j], names[j+1]
        # # heights = sorted(heights, reverse = True)
        return names
        ans = [hashmap[heights[i]] for i in range(len(heights))]

        
        
        