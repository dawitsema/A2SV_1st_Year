class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dictionary = Counter(answers)
        rabits = 0
        for key in dictionary:
            if key == 0:
                rabits += dictionary[key]
            elif key == 1:
                if dictionary[key]%2 == 0:
                    rabits += dictionary[key]
                else:
                    rabits += dictionary[key] + 1
            else:
                if dictionary[key] <= key + 1:
                    rabits += key + 1
                else:
                    temp = dictionary[key]//(key + 1) + 1
                    rabits += (key + 1) * temp 

        return rabits



        