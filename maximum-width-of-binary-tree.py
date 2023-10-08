# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        d = defaultdict(list)
        def helper(root, row,idx):
            nonlocal d
            if root:
                d[row].append(idx)
                helper(root.left, row+1, 2*idx)
                helper(root.right, row+1, 2*idx+1)
        helper(root,0,0)
        #print(d)
        _max = 0
        for k,v in d.items():
            _max = max((v[-1] - v[0])+1, _max)
        return _max