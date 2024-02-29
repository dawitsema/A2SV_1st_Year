# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(node, dic, a, b):
            if not node:
                return {}

            a = min(a, node.val)
            b = max(b, node.val)
            dic[node.val] = [a, b]

            helper(node.left, dic, a, b)
            helper(node.right, dic, a, b)

            return dic

        dictionary = helper(root, {}, float("inf"), float("-inf"))
        maxx = 0
        for key in dictionary:
            maxx = max(maxx, dictionary[key][1] - dictionary[key][0])
        
        return maxx
            
        