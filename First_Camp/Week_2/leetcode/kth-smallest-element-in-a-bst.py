# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(node, box):
            if not node:
                return []
            helper(node.left, box)
            box.append(node.val)
            helper(node.right, box)

            return box
        
        return helper(root, [])[k-1]

        