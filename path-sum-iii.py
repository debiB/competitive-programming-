# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        total = 0 
        def helper(node, _sum):
            nonlocal total
            if not node:
                return 
            if _sum == node.val:
                total +=1
            helper(node.left, _sum - node.val)
            helper(node.right, _sum - node.val)
        def dfs(root):
            if not root:
                return 
            helper(root,targetSum)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return total