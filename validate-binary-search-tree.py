# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root, lower_bound, upper_bound):
            if not root:
                return True
            if (root.val >= upper_bound) or (root.val <= lower_bound):
                return False 
            else:
                return helper(root.left, lower_bound,root.val) and helper(root.right, root.val, upper_bound)
        return helper(root,-inf,inf)