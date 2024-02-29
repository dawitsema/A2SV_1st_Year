# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(node, box, key):
            if not node:
                return
            box.append(node)
            if node.val == key:
                return box
            elif node.val > key:
                return find(node.left, box, key)
            else:
                return find(node.right, box, key)

        box1 = find(root, [], p.val)
        box2 = find(root, [], q.val)
        
        pt1 = 0
        pt2 = 0
        n = len(box1)
        m = len(box2)
        ans = None
        while pt1 < n and pt2 < m:
            if box1[pt1].val == box2[pt2].val:
                ans = box1[pt1]
            else:
                break
            pt1 += 1
            pt2 += 1
            

        return ans

