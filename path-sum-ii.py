# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        
        def dfs(root, li):
            if not root:
                return
            
            li.append(root.val)
            
        
            if not root.left and not root.right and sum(li) == targetSum:
                ans.append(li.copy())  
            
            dfs(root.left, li)
            dfs(root.right, li)
            
            li.pop()  
        
        dfs(root, [])
        return ans