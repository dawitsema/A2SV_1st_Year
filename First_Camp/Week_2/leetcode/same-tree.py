class Solution:
    def isSameTree(self, p, q):
        def helper(a, b):
            if not a and not b:
                return True
            elif not a or not b:
                return False
            elif a.val == b.val:
                return helper(a.left, b.left) and helper(a.right, b.right)
            return False
        
        return helper(p, q)
        