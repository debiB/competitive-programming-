# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total_sum= 0 
        def helper(root, curr):
            nonlocal total_sum
            if not root:
                n= curr
                total_sum += n
                return
            curr = curr*10 + root.val
            helper(root.left,curr)
           # curr = curr//10
            helper(root.right,curr)
        helper(root, 0)
        return total_sum//2