# Find All Possible Recipes from Given Supplies
# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/
# Accepted 2023-04-25 17:03 UTC · Python · 901 ms · 17.2 MB

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        receipes = set(recipes)
        adj = defaultdict(list)
        indegree = {dish: len(reqs) for reqs, dish in zip(ingredients, recipes)}
        for reqs, dish in zip(ingredients, recipes):
            for req in reqs:
                adj[req].append(dish)
        all_ingredients = set([e for row in ingredients for e in row])
        queue = deque([supply for supply in supplies if supply in all_ingredients])
        visited = set()
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
                    if v in recipes:
                        visited.add(v)
        return visited
