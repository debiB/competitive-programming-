class ThroneInheritance:

    def __init__(self, kingName: str):
       self.king = kingName
       self.children = defaultdict(list)
       self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        ans = []
        def dfs(name):
            nonlocal ans
            if name not in self.dead:
                ans.append(name)
            for child in self.children[name]:
                dfs(child)
        dfs(self.king)
        return ans
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()