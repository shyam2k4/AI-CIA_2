class BranchAndBoundWithExtendedList:
    def __init__(self, edges, oracle):
        self.edges = edges
        self.graph_dict = {}
        self.oracle = oracle
        self.best_path = None

        for start, end, cost in self.edges:
            if start not in self.graph_dict:
                self.graph_dict[start] = []
            self.graph_dict[start].append((cost, end))

    def find_paths(self, start, end, path=[], cost=0):
        path = path + [start]

        if start == end:
            if (self.oracle[0] is None) or (cost == self.oracle[0]):
                self.oracle[0] = cost
                if self.best_path is None or cost < self.best_path[0]:
                    self.best_path = (cost, path.copy())
            return

        if start not in self.graph_dict:
            return

        for edge_cost, neighbor in self.graph_dict[start]:
            if neighbor not in path:
                self.find_paths(neighbor, end, path, cost + edge_cost)

    def show_paths(self, start, end):
        self.find_paths(start, end)
        
        if self.best_path is not None:
            cost, path = self.best_path
            path.pop(0)
            print("Path derived by Branch And Bound With Extended List Algorithm:")
            print(" -> ".join(path))
        else:
            print("No valid path found.")

# Define the edges and oracle with updated values
edges_with_cost = [('S', 'B', 5), ('S', 'A', 4), ('A', 'B', 3), ('B', 'A', 3),
                   ('A', 'D', 5), ('D', 'F', 2), ('B', 'C', 4), ('C', 'E', 5), ('F', 'G', 1)]
oracle_values = [12]

# Create a BranchAndBoundWithExtendedList object and find the paths
bnbwl = BranchAndBoundWithExtendedList(edges_with_cost, oracle_values)
bnbwl.show_paths('S', 'G')
