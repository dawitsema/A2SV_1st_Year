class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def compare(radius):
            pt1 = pt2 = 0
            while pt1 < len(houses) and pt2 < len(heaters):
                if abs(houses[pt1] - heaters[pt2]) <= radius:
                    pt1 += 1
                else:
                    pt2 += 1
            if pt1 == len(houses):
                return True
            else:
                return False
            

        low, high = 0, max(houses[-1], heaters[-1])
        ans = high
        while low <= high:
            midd = (low + high)//2
            result = compare(midd)

            if result:
                ans = midd
                high = midd - 1
            else:
                low = midd + 1

        return ans
