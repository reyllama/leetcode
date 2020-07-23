"""
785. Is Graph Bipartite?


Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation:
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation:
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.


Note:

graph will have length in range [1, 100].
graph[i] will contain integers in range [0, graph.length - 1].
graph[i] will not contain i or duplicate values.
The graph is undirected: if any element j is in graph[i], then i will be in graph[j].
"""

class Solution:
    def helper(self, graph, source):
        queue = [source]

        while queue:
            cur = queue.pop()

            for v in range(len(graph)):
                if (v in graph[cur]) & (self.colors[v]==-1):
                    self.colors[v] = 1-self.colors[cur]
                    queue.append(v)
                elif (v in graph[cur]) & (self.colors[v]==self.colors[cur]):
                    return False

        return True

    def isBipartite(self, graph):
        self.colors = [-1] * len(graph)
        for i in range(len(graph)):
            if self.colors[i] == -1:
                if not self.helper(graph, i):
                    return False
        return True

"""
Runtime: 1136 ms, faster than 5.09% of Python3 online submissions for Is Graph Bipartite?. O(n^2)
Memory Usage: 14.2 MB, less than 49.93% of Python3 online submissions for Is Graph Bipartite?.
"""
from collections import defaultdict
class Solution:
    def isBipartite(self, graph):
        color = defaultdict(lambda: -1)
        return all(self.dfs(graph, v, edges, 0, color) for v, edges in enumerate(graph) if color[v] == -1)

    def dfs(self, graph, v, edges, cur_color, color):
        if color[v] != -1: return color[v] == cur_color
        color[v] = cur_color
        return all(self.dfs(graph, e, graph[e], 1-cur_color, color) for e in edges)

"""
Runtime: 224 ms, faster than 40.71% of Python3 online submissions for Is Graph Bipartite?.
Memory Usage: 14.2 MB, less than 48.02% of Python3 online submissions for Is Graph Bipartite?.
"""

x = Solution()
g = [[1],[0],[4],[4],[2,3]]
print(x.isBipartite(g))
# print((set([3]) & set([0,2])) & (set([3]) & set([1]) == None))
# print(set([3]) & set([0,3]))
