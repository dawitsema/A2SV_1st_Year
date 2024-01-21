class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        all_book = [0]*(n + 2)
        for book in bookings:
            all_book[book[0]] += book[2]
            all_book[book[1] + 1] -= book[2]

        answer = [all_book[1]]
        for i in range(1, n):
            answer.append(answer[-1] + all_book[i + 1])
        
        return answer

        
        