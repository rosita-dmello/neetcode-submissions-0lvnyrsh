class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            course_map[c].append(p)
            
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if course_map[course] == []:
                return True
            
            visited.add(course)
            for crs in course_map[course]:
                if not dfs(crs): return False
            visited.remove(course)
            course_map[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c): return False
        
        return True