# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxx = float('-inf')
        def summ(root):
            nonlocal maxx
            if not root:
                return 0
            
            sum1 = max(summ(root.right), 0)
            sum2 = max(summ(root.left), 0)


            maxx = max(maxx, root.val + sum1 + sum2)

            return root.val + max(sum1, sum2)
        
        summ(root)
        return maxx