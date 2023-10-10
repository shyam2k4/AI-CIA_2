class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, priority, item):
        self.queue.append((priority, item))
        self.queue.sort(key=lambda x: x[0])

    def pop(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Priority queue is empty")

    def is_empty(self):
        return len(self.queue) == 0


class BeamSearch:
    def __init__(self, edges):
        self.graph_dict = {}
        for start, end, cost in edges:
            self.graph_dict.setdefault(start, []).append((end, cost))

    def beam_search(self, start, end, beam_width=1):
        beam = PriorityQueue()
        beam.push(0, [start])

        while not beam.is_empty():
            cost, path = beam.pop()

            current_node = path[-1]

            if current_node == end:
                return path

            if current_node in self.graph_dict:
                neighbors = self.graph_dict[current_node]
                neighbors.sort(key=lambda x: x[1])
                for neighbor, edge_cost in neighbors[:beam_width]:
                    new_path = path + [neighbor]
                    new_cost = cost + edge_cost
                    beam.push(new_cost, new_path)

        return []

    def show_path(self, start, end, beam_width=1):
        path = self.beam_search(start, end, beam_width)
        if path:
            print("Path derived by Beam Search Algorithm:")
            print(" -> ".join(path))
        else:
            print("No valid path found.")


# Define the edges with updated values
edges_with_cost = [('S', 'B', 5), ('S', 'A', 4), ('A', 'B', 3), ('B', 'A', 3),
                   ('A', 'D', 5), ('D', 'F', 2), ('B', 'C', 4), ('C', 'E', 5), ('F', 'G', 1)]

beam_search = BeamSearch(edges_with_cost)
beam_search.show_path('S', 'G', beam_width=2)
