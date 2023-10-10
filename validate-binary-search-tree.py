# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, lower_bound, upper_bound):
        if not root:
            return True
        elif(root.val <= lower_bound or root.val >= upper_bound):
            return False
        else:
            return self.helper(root.left, lower_bound, root.val) and self.helper(root.right, root.val, upper_bound)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
       return self.helper(root, -inf, inf)