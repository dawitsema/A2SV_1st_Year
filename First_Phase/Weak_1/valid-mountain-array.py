class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        l = 0
        r = len(arr) - 1
        if len(arr) < 3:
            return False
        
        while arr[l] < arr[l+1] and l < len(arr) - 2:
            l += 1
        while arr[r] < arr[r-1] and r > 1:
            r -= 1
        return l == r
        