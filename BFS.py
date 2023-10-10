from collections import defaultdict

class BFS:
    def __init__(self, edges):
        self.graph = defaultdict(list)
        for start, end in edges:
            self.graph[start].append(end)

    def find_path(self, start, end):
        visited = set()
        queue = [[start]]

        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node == end:
                return path

            if node not in visited:
                for neighbor in self.graph[node]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

                visited.add(node)

        return []

    def show_path(self, start, end):
        path = self.find_path(start, end)
        if path:
            print("Path derived by Breadth-First Search Algorithm:")
            print(" -> ".join(path))
        else:
            print("No valid path found.")

# Define the edges for BFS
edges_bfs = [('S', 'B'), ('S', 'A'), ('A', 'B'), ('B', 'A'), ('A', 'D'), ('D', 'F'), ('B', 'C'), ('C', 'E'), ('F', 'G')]

# Create a BFS object and find the path
bfs = BFS(edges_bfs)
bfs.show_path('S', 'G')
