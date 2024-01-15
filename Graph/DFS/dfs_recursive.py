from collections import defaultdict
class DFS:
    def __init__(self, n, edges):    
        self.graph = defaultdict(list)
        self.n = n
        self.visited = set()
        self.res = []
        for (src, dst) in edges:
            self.graph[src].append(dst)
            
    def dfs(self, node):
        self.visited.add(node)
        self.res.append(node)
        for neighbor in self.graph[node]:
            if neighbor not in self.visited:
                self.dfs(neighbor)
                    
    def dfs_recursive(self, n):
        for i in range(1, n+1):
            if i not in self.visited:
                self.dfs(i)
        return self.res
n = 6
cities = [(1,3), (1,2), (2,4), (3,5), (4,6)]
obj = DFS(n, cities)
print(obj.dfs_recursive(n))
