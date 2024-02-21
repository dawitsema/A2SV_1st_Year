class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        right, left = 0, 0
        count = 0
        while right < len(points):
            count += 1
            temp = points[left]
            while right < len(points) and temp[1] >= points[right][0]:
                right += 1
            
            left = right 
        
        return count

        