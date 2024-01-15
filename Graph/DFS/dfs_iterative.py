from collections import defaultdict

class Graph:
    """
    Approach: Iterative DFS using stack
    TC: O(E)
    SC: O(V)
    """
    def __init__(self, n, edges):
        self.n = n
        self.graph = defaultdict(list)
        # use set for visited for O(1) lookup
        # or use visited = [False for i in range(self.n)]
        self.visited = set()
        self.res = []

        # add edges for undirected graph
        for (src, dst) in edges:
            self.graph[src].append(dst)
            self.graph[dst].append(src)

    def dfs(self, node):
        stack = [node]
        self.visited.add(node)

        while stack:
            node = stack.pop()
            self.res.append(node)
            for adj in self.graph[node]:
                if adj not in self.visited:
                    stack.append(adj)
                    self.visited.add(adj)

    # call DFS on every node for disconnected graph
    def dfs_iterative(self):
        for i in range(self.n):
            if i not in self.visited:
                self.dfs(i)
        return self.res
n = 6
edges = [(1, 0), (3, 4), (0, 2), (5, 5), (1, 2)]
obj = Graph(n, edges)
print(obj.dfs_iterative())




    