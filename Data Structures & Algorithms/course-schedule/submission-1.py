class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = [0] * numCourses
        adjList = {i: [] for i in range(numCourses)}

        for src, dest in prerequisites:
            adjList[src].append(dest)
            indegree[dest] += 1
        q = collections.deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        finish = 0
        while q:
            crs = q.popleft()
            finish += 1
            for nei in adjList[crs]:
                indegree[nei] -=1
                if indegree[nei] == 0:
                    q.append(nei)
        return finish == numCourses