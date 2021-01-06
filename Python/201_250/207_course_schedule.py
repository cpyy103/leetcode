from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degrees = [0 for i in range(numCourses)]
        adjacency = [[] for i in range(numCourses)]

        queue = []
        for cur, pre in prerequisites:
            in_degrees[cur] += 1
            adjacency[pre].append(cur)

        for i in range(len(in_degrees)):
            if not in_degrees[i]:
                queue.append(i)

        while queue:
            pre = queue.pop(0)
            numCourses -= 1
            for cur in adjacency[pre]:
                in_degrees[cur] -= 1
                if not in_degrees[cur]:
                    queue.append(cur)

        return not numCourses


if __name__ == '__main__':
    numCourses = 2
    prerequisties = [[1, 0]]
    print(Solution().canFinish(numCourses, prerequisties))
