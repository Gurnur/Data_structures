from collections import defaultdict, deque
class BFS:
    def __init__(self, n, edges):
        self.n = n
        self.graph = defaultdict(list)
        self.visited = set()
        self.res = []

        for (src,dst) in edges:
            self.graph[src].append(dst)

    def bfs(self, node):
        queue = deque()
        queue.append(node)
        self.visited.add(node)

        while queue:
            node = queue.popleft()
            self.res.append(node)
            for neighbor in self.graph[node]:
                if neighbor not in self.visited:
                    queue.append(neighbor)
                    self.visited.add(neighbor)

    def bfs_iterative(self, n):
        for i in range(1, n+1):
            if i not in self.visited:
                self.bfs(i)
        return self.res

n = 6
cities = [(1,3), (2,1), (4,2), (3,5), (6,4)]
obj = BFS(n, cities)
print(obj.bfs_iterative(n))
