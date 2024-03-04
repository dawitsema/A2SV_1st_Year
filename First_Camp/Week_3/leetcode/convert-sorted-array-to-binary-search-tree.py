# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(left, right):
            if left > right:
                return None

            midd = (left + right)//2
            node = TreeNode(nums[midd])
            node.left = helper(left, midd - 1)
            node.right = helper(midd + 1, right)

            return node
        
        n = len(nums)
        return helper(0, n-1)