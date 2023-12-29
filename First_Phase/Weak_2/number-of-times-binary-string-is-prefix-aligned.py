class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        fliped = 0
        count = 0
        _max = 0

        for flip in flips:
            fliped += 1
            _max = max(flip, _max)
            if fliped >= _max:
                count += 1
        
        return count
        
 


                
        