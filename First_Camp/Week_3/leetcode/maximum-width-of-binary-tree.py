# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dictionary = defaultdict(list)

        def helper(node, val, depth):
            if not node:
                return []
            dictionary[depth].append(val)
            helper(node.left, 2*val + 1, depth + 1)
            helper(node.right, 2*val + 2, depth + 1)


        helper(root, 0, 0)
        ans = 0
        for val in dictionary.values():
            ans = max(ans, val[-1] - val[0] + 1)
        
        return ans

            
            