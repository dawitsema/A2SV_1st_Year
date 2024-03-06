class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ind = bisect_right(letters, target)
        ans = letters[ind] if ind < len(letters) else letters[0]
        return ans
