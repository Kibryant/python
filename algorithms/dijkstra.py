import heapq


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = {}

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node][to_node] = distance
        self.edges[to_node][from_node] = distance


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


if __name__ == "__main__":
    graph = Graph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_node("E")
    graph.add_node("F")

    graph.add_edge("A", "B", 4)
    graph.add_edge("A", "C", 2)
    graph.add_edge("B", "C", 5)
    graph.add_edge("B", "D", 10)
    graph.add_edge("C", "E", 3)
    graph.add_edge("D", "E", 4)
    graph.add_edge("D", "F", 11)
    graph.add_edge("E", "F", 5)

    print(
        dijkstra(graph.edges, "A")
    )  # {'A': 0, 'B': 4, 'C': 2, 'D': 9, 'E': 5, 'F': 10}
