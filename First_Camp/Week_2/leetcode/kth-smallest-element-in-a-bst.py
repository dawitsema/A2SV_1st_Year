# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(node):
            # nonlocal box
            if not node:
                return []
            helper(node.left)
            box.append(node.val)
            helper(node.right)

            # return box
        box = []
        helper(root)
        return box[k-1]

        