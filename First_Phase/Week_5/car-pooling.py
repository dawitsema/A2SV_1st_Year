
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        dist = [0] * 1001
        
        for trip in trips:
            dist[trip[1]] += trip[0]
            dist[trip[2]] -= trip[0]

        answer = [0]
        for i in range(1001):
            answer.append(answer[-1] + dist[i])
            
            if answer[i] > capacity:
                return False

        return True
