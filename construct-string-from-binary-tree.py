# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = []
        def dfs(root):
            nonlocal ans
            if not root:
                return  
            ans.append('(')
            ans.append(str(root.val))
            if not root.left and root.right:
                ans.append("()") 
            dfs(root.left)
            dfs(root.right)
            ans.append(")")
        dfs(root)
        return "".join(ans)[1:-1]