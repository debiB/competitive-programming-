# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
       
        adj = defaultdict(list)
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                adj[node.left.val].append(node.val)
                adj[node.val].append(node.left.val)
                q.append(node.left)
            if node.right:
                adj[node.right.val].append(node.val)
                adj[node.val].append(node.right.val)
                q.append(node.right)
        visited = set([target.val])
        q= deque([target.val])
        while k and q:
            for _ in range(len(q)):
                curr = q.popleft()
                for n in adj[curr]:
                    if n not in visited:
                        q.append(n)
                        visited.add(n)
            k-=1
        return list(q)