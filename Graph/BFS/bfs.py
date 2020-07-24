from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, source):
        visited = [False] * len(self.graph)

        queue = deque()

        queue.append(source)
        visited[source] = True

        while queue:
            adj_node = queue.popleft()
            print(" ", adj_node)
            for i in self.graph[adj_node]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

g = Graph()
g.add_edge(0, 1) 
g.add_edge(0, 2) 
g.add_edge(1, 2) 
g.add_edge(2, 0) 
g.add_edge(2, 3) 
g.add_edge(3, 3)

g.bfs(2)
