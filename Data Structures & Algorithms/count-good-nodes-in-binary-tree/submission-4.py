# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, maxx: int):
            if not root:
                return 0
            
            total = 0
            if root.val >= maxx:
                total += 1
            
            new_max = max(maxx, root.val)
            total += dfs(root.left, new_max)
            total += dfs(root.right, new_max)

            return total
        
        result = dfs(root, float('-inf'))
        return result
