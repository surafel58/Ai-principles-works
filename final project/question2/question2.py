from collections import deque
import heapq

class StateSpaceGraph:
    def __init__(self):
        # Representing the state space graph as an adjacency list with weights
        self.graph = {}

    def add_edge(self, source, destination, cost):
        if source not in self.graph:
            self.graph[source] = []
        if destination not in self.graph:
            self.graph[destination] = []
        self.graph[source].append((destination, cost))
        self.graph[destination].append((source, cost))  # Since the graph is undirected

    def uniform_cost_search(self, start, goal):
        # Priority queue for UCS
        priority_queue = [(0, start, [start])]  # (cost, current_node, path)
        visited = set()

        while priority_queue:
            cost, current_node, path = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node == goal:
                return cost, path

            for neighbor, edge_cost in self.graph.get(current_node, []):
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (cost + edge_cost, neighbor, path + [neighbor]))

        return float("inf"), []  # Return infinity and empty path if no solution

    def multi_goal_ucs(self, start, goals):
        remaining_goals = set(goals)
        current_state = start
        total_cost = 0
        complete_path = [start]  # Initialize with the start state

        while remaining_goals:
            min_cost = float('inf')
            best_goal = None
            best_path = None # Initialize best_path to None

            for goal in remaining_goals:
                cost, path = self.uniform_cost_search(current_state, goal)
                if cost < min_cost:
                    min_cost = cost
                    best_goal = goal
                    best_path = path

            if best_goal is None or min_cost == float('inf'):
                print(f"Error: Unreachable goals detected from '{current_state}' to {remaining_goals}")
                return float('inf'), []

            total_cost += min_cost
            if best_path:
                complete_path.extend(best_path[1:])  # Extend correctly, avoiding duplication
            current_state = best_goal
            remaining_goals.remove(best_goal)

        return total_cost, complete_path

