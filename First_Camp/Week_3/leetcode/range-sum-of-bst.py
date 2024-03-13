# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.summ = 0
        def helper(node):
            if not node:
                return
                
            if node.val >= low and node.val <= high:
                self.summ += node.val
            helper(node.left)
            helper(node.right)

            return 0

        helper(root)
        return self.summ