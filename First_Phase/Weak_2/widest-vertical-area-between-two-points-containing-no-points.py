class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        st = [None]*len(points)
        for i in range(len(points)):
            st[i] = points[i][0]

        st.sort()

        temp = 0
        for i in range(len(points)-1):
            temp = max(temp, st[i+1] - st[i])
            
        return temp


        