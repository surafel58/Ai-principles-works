import heapq

class StateSpaceGraph:
    def __init__(self):
        self.graph = {}
        self.heuristics = {}

    def add_edge(self, source, destination, cost):
        if source not in self.graph:
            self.graph[source] = []
        if destination not in self.graph:
            self.graph[destination] = []
            
        self.graph[source].append((destination, cost))
        self.graph[destination].append((source, cost))

    def set_heuristic(self, node, heuristic):
        self.heuristics[node] = heuristic

    def a_star_search(self, start, goal):
        # Priority queue for A*
        # (f_cost, g_cost, current_node, path)
        priority_queue = [(self.heuristics[start], 0, start, [start])]
        visited = set()

        while priority_queue:
            f_cost, g_cost, current_node, path = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node == goal:
                return g_cost, path

            for neighbor, edge_cost in self.graph.get(current_node, []):
                if neighbor not in visited:
                    g = g_cost + edge_cost
                    f = g + self.heuristics.get(neighbor, float('inf'))
                    heapq.heappush(priority_queue, (f, g, neighbor, path + [neighbor]))

        # Return infinity and empty path if no solution  
        return float("inf"), []