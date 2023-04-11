"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        total_ans = 0
        d = {e.id:e for e in employees}
        def helper(id):
            nonlocal total_ans
            n= d[id]
            total_ans += n.importance
            for i in n.subordinates:
                helper(i)
        helper(id)
        return total_ans