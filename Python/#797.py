"""
797. All Paths From Source to Target

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1, and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

 """

 class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        def route(progress):

            if progress[-1] == n-1:
                sol.append(progress)
                return
            else:
                for node in graph[progress[-1]]:
                    route(progress + [node])

        sol = []
        n = len(graph)

        route([0])
        return sol

"""
Runtime: 88 ms, faster than 99.04% of Python3 online submissions for All Paths From Source to Target.
Memory Usage: 15.6 MB, less than 74.45% of Python3 online submissions for All Paths From Source to Target.
"""
