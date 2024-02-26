# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def BST(node, counter):
            if not node:
                return
            BST(node.left, counter)
            counter[node.val] += 1
            BST(node.right, counter)
        
        counter = defaultdict(int)
        BST(root, counter)
        maxx = max(counter.values())

        ans = []
        for key in counter:
            if counter[key] == maxx:
                ans.append(key)
        return ans
        