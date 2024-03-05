class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []

        def helper(s, left, right):
            if left == 0 and right == 0:
                ans.append(s)

            if left > 0:
                helper(s + "(", left - 1, right)

            if right > 0 and left < right:
                helper(s + ")", left, right - 1)

        ans = []
        helper("", n, n)

        return ans
