# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def helper(node, key):
            if not node:
                return

            if node.val == key:
                return node
            elif node.val > key:
                return helper(node.left, key)
            else:
                return helper(node.right, key)
        
        return helper(root, val)
            
            