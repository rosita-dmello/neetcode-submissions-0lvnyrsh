class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = {c: [] for c in range(numCourses)}
        op = []

        for crs, pre in prerequisites:
            prereqs[crs].append(pre)

        visited, cycle = set(), set()
        def dfs(c):
            if c in visited:
                return True
            if c in cycle:
                return False

            cycle.add(c)
            for p in prereqs[c]:
                if not dfs(p):
                    return False
            cycle.remove(c)
            visited.add(c)
            op.append(c)

            return True
            
        for course in range(numCourses):
            if not dfs(course):
                return []
        return op

