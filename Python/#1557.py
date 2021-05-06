"""
1557. Minimum Number of Vertices to Reach All Nodes

Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.
"""

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ref = dict()
        for i in range(n):
            ref[i] = 0
        for s, e in edges:
            ref[e] += 1
        return [key for key in ref.keys() if ref[key]==0]

"""
Runtime: 1232 ms, faster than 20.94% of Python3 online submissions for Minimum Number of Vertices to Reach All Nodes.
Memory Usage: 53.3 MB, less than 33.19% of Python3 online submissions for Minimum Number of Vertices to Reach All Nodes.
"""

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        return list(set(range(n)) - set(j for i, j in edges))

"""
Runtime: 1136 ms, faster than 92.88% of Python3 online submissions for Minimum Number of Vertices to Reach All Nodes.
Memory Usage: 52.8 MB, less than 78.85% of Python3 online submissions for Minimum Number of Vertices to Reach All Nodes.
"""
