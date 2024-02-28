# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(nodeA, nodeB, newNode):
            if not nodeA and not nodeB:
                return 
            if nodeA and nodeB:
                newNode = TreeNode(nodeA.val + nodeB.val)
                newNode.left = helper(nodeA.left, nodeB.left, newNode)
                newNode.right = helper(nodeA.right, nodeB.right, newNode)
            elif nodeA:
                newNode = nodeA
            elif nodeB:
                newNode = nodeB
            
            return newNode

        ans = TreeNode()
        return helper(root1, root2, ans)                