import heapq


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append(vertex2)
            self.vertices[vertex2].append(vertex1)

    def get_neighbors(self, vertex):
        if vertex in self.vertices:
            return self.vertices[vertex]
        else:
            return []

    def shortest_path(self, start, end):
        distances = {vertex: float("inf") for vertex in self.vertices}
        distances[start] = 0
        queue = [(0, start)]
        while queue:
            current_distance, current_vertex = heapq.heappop(queue)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor in self.get_neighbors(current_vertex):
                distance = current_distance + 1
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))
        return distances[end]

    def __str__(self):
        return str(self.vertices)


if __name__ == "__main__":
    g = Graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")
    g.add_vertex("F")
    g.add_vertex("G")
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "E")
    g.add_edge("D", "F")
    g.add_edge("E", "F")
    g.add_edge("F", "G")
    print(g.shortest_path("A", "G"))  # 3
    print(g.shortest_path("A", "D"))  # 2
    print(g.shortest_path("A", "E"))  # 2
    print(g.shortest_path("A", "F"))  # 3
    print(g.shortest_path("A", "B"))  # 1
    print(g.shortest_path("A", "C"))  # 1
    print(g.shortest_path("A", "A"))  # 0
    print(g.shortest_path("A", "Z"))  # inf
    print(g.shortest_path("Z", "A"))  # inf
    print(g.shortest_path("Z", "Z"))  # 0
    print(g)
