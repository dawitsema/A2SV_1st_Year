class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
            elif s[i] == ")":
                if len(stack) == 0:
                    stack.append(s[i])
                else:
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        stack.append(s[i])
            
        
        return len(stack)


        