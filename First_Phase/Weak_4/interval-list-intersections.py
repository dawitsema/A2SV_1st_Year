class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first = second = 0
        ans = []
        while first < len(firstList) and second < len(secondList):
            temp = [0]*2
            if firstList[first][0] <= secondList[second][1] and firstList[first][1] >= secondList[second][0]:
                temp[0] = max(firstList[first][0], secondList[second][0])
                temp[1] = min(secondList[second][1], firstList[first][1])
                ans.append(temp)

            if firstList[first][1] > secondList[second][1]:
                second += 1
            else:
                first += 1
        
        return ans
            





