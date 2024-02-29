# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(node, box, depth):
            if not node:
                return []
            box.append([depth, node.val])
            helper(node.left, box, depth + 1)
            helper(node.right, box, depth + 1)

            return box
        
        array = helper(root, [], 0)
        dictionary = defaultdict(list)
        print(array)
        for i in range(len(array)):
            dictionary[array[i][0]].append(array[i][1])

        ans = []
        for key in dictionary:
            if key%2 == 0:
                ans.append(dictionary[key])
            else:
                ans.append(reversed(dictionary[key]))

        return ans

        # array.sort()
        # pt = 0
        # ans = []
        # temp = []
        # pt2 = array[pt][0]

        # while pt < len(array):
        #     pt2 = array[pt][0]
        #     if temp:
        #         if (pt2-1)%2 == 0:
        #             ans.append(temp)
        #         else:
        #             ans.append(temp.reverse())

        #     temp = []
        #     while pt < len(array) and pt2 == array[pt][0]:
        #         temp.append(array[pt][1])
        #         pt += 1
        # if temp:
        #     if (pt2-1)%2 == 0:
        #         ans.append(temp)
        #     else:
        #         ans.append(temp.reverse())

            
        # return ans