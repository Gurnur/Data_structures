from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_recur(self, source, visited):
        visited[source] = True
        print(source)

        for i in self.graph[source]:
            if visited[i] == False:
                self.dfs_recur(i, visited)

    def dfs(self):
        v = len(self.graph) + 1
        visited = [False] * (v)

        for i in range(v):
            if visited[i] == False:
                self.dfs_recur(i, visited)

g = Graph()
g.add_edge(0, 1) 
g.add_edge(0, 2) 
g.add_edge(1, 2) 
g.add_edge(2, 0) 
g.add_edge(2, 3) 
g.add_edge(3, 3) 
g.add_edge(4, 5)
g.add_edge(4, 3)

g.dfs()