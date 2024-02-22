class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if len(stack) != 0:
                    if dictionary[ch] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        return len(stack) == 0

        