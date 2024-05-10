# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        zigzag= False
        ans = []
        q = deque([root])
        while q:
            
            res = []
            length = len(q)
            for i in range(length):
                node = q.popleft()
                res.append(node.val)
                if node.left:
                        q.append(node.left)
                if node.right:
                        q.append(node.right)
            if zigzag:
                res = res[::-1]
            zigzag = not zigzag
            ans.append(res)
        return ans