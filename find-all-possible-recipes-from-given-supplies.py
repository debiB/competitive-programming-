class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies) 
        d = defaultdict(list)
        indeg = defaultdict(int)
        ans = []
        q = deque()
        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                d[ingredients[i][j]].append(recipes[i])
                indeg[recipes[i]]+=1
        for k in supplies:
            q.append(k)
        recipes = set(recipes)
    
        while q:
            res = q.popleft()
            if res in recipes:
                ans.append(res)
            for child in d[res]:
                indeg[child]-=1
                if indeg[child] == 0:
                    q.append(child)
        return ans