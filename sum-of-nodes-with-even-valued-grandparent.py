# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        li = []
        ans = 0
        def helper(root):
            if not root:
                return 
            if root.val %2 == 0:
                li.append(root)
            helper(root.left)
            helper(root.right)
        helper(root)
        for i in li:
            if i.left:
                if i.left.left:
                    ans+= i.left.left.val
                if i.left.right:
                    ans+= i.left.right.val
            if i.right:
                if i.right.left:
                    ans+= i.right.left.val
                if i.right.right:
                    ans+= i.right.right.val
        return ans