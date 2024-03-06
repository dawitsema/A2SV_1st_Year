# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        box = []
        def helper(node):
            if not node:
                return
            helper(node.left)
            box.append(node.val)
            helper(node.right)
        
        helper(root)
        def build(high, low):
            if low > high:
                return
            mid = (low + high)//2
            node = TreeNode(box[mid])
            node.left = build(mid - 1, low)
            node.right = build(high, mid + 1)

            return node

        return build(len(box) - 1, 0)

        