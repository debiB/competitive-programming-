from typing import List
from collections import defaultdict, deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegrees = [0] * numCourses
        prerequisites_map = defaultdict(set)

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegrees[course] += 1

        queue = deque()
        for course in range(numCourses):
            if indegrees[course] == 0:
                queue.append(course)

        while queue:
            prerequisite = queue.popleft()
            for course in graph[prerequisite]:
                indegrees[course] -= 1
                prerequisites_map[course].add(prerequisite)
                prerequisites_map[course] |= prerequisites_map[prerequisite]
                if indegrees[course] == 0:
                    queue.append(course)

        result = []
        for query in queries:
            course, prerequisite = query
            result.append(prerequisite in prerequisites_map[course])

        return result