class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat_number = 0
        people.sort()

        right = len(people)-1
        left = 0
        while left <= right:
            if people[right] + people[left] <= limit:
                boat_number += 1
                right -= 1
                left += 1
            else:
                boat_number += 1
                right -= 1
            
        return boat_number

        