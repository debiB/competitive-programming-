# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        q = deque([root])
        while q:
            total = 0
            curr = len(q)
            for _ in range(len(q)):
                num = q.popleft()
                total+= num.val 

                if num.left:
                    q.append(num.left)
                if num.right:
                    q.append(num.right)
            ave = total/ curr
            ans.append(ave)
        return ans