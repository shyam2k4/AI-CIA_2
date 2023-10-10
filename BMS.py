class BMS:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for i, j in self.edges:
            if i not in self.graph_dict:
                self.graph_dict[i] = [j]
            else:
                self.graph_dict[i].append(j)
    def find_paths(self, start, end, path=[]):
        paths = []
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        sorted_nodes = sorted(self.graph_dict[start])
        for node in sorted_nodes:
            if node not in path:
                new_paths = self.find_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths
    def show_paths(self, start, end):
        paths = self.find_paths(start, end)
        print("Paths derived by British Museum Search Algorithm:")
        for path in paths:
            print(" -> ".join(path))
edges_bms = [('S', 'B'), ('S', 'A'), ('A', 'B'), ('B', 'A'), ('A', 'D'), ('D', 'F'), ('B', 'C'), ('C', 'E'), ('F', 'G')]
bms = BMS(edges_bms)
bms.show_paths('S', 'G')
