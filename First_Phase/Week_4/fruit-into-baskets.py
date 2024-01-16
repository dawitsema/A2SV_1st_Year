class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        check = set()
        count = maxx = 0
        left = 0
        n = len(fruits)
        for right in range(n):
            check.add(fruits[right])
            count += 1
            if len(check) > 2:
                left = right - 1
                count = 1
                while fruits[right - 1] == fruits[left]:
                    count += 1
                    left -= 1
                check.remove(fruits[left])
                left += 1
             
            maxx = max(maxx, count)
        
        return maxx
            




        
        


        