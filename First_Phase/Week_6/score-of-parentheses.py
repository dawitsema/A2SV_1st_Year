class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for ch in s:
            if ch == "(":
                stack.append(ch)
            else:
                val = 0
                if stack[-1] == "(":
                    stack.pop()
                    val = 1
                else:
                    val = int(stack.pop())
                    if stack[-1] == '(':
                        val *= 2
                        stack.pop()
                while stack and stack[-1].isdigit():
                    val += int(stack.pop())
                stack.append(str(val))

                
        return int(stack[-1])
        