# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, box):
            if not node:
                return
            helper(node.left, box)
            box.append(node.val)
            helper(node.right, box)
            return box
        
        array = helper(root, [])
        for i in range(len(array) - 1):
            if array[i] < array[i+1]:
                continue
            else:
                return False
        
        return True


        