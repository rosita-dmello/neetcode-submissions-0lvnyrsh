class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0] * numCourses
        adjList = {i: [] for i in range(numCourses)}

        for src, dest in prerequisites:
            adjList[src].append(dest)
            indegree[dest] += 1
        q = collections.deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        ordering = []
        while q:
            crs = q.popleft()
            ordering.append(crs)
            for nei in adjList[crs]:
                indegree[nei] -=1
                if indegree[nei] == 0:
                    q.append(nei)

        return ordering[::-1] if (len(ordering) == numCourses) else []