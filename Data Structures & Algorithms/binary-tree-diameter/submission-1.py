# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #length = number of nodes - 1
        largest_diameter = 0
        
        def height(root):
            nonlocal largest_diameter
            if not root:
                return 0
            right = height(root.right)
            left = height(root.left)
            diameter = right + left

            largest_diameter = max(largest_diameter, diameter)

            return 1 + max(right, left)
        
        height(root)
        return largest_diameter
            

        

        
        