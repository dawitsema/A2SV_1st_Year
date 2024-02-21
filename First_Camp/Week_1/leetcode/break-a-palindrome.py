class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""

        countA = palindrome.count("a")
        for i in range(len(palindrome)):
            if palindrome[i] != 'a' and len(palindrome) - countA != 1:
                ans = palindrome[:i] + "a" + palindrome[i+1:]
                break
            if i == len(palindrome) - 1:
                ans = palindrome[:i] + 'b'

        return ans
        
        
                
        