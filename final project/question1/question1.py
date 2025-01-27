from collections import deque

class StateSpaceGraph:
    def __init__(self):
        # Representing the state space graph as an adjacency list
        self.graph = {}

    def add_edge(self, source, destination):
        if source not in self.graph:
            self.graph[source] = []
        if destination not in self.graph:
            self.graph[destination] = []
        self.graph[source].append(destination)
        self.graph[destination].append(source)

    def bfs(self, start, goal):
        # Breadth-First Search implementation
        queue = deque([(start, [start])])  # Queue stores (current_node, path)
        visited = set()

        while queue:
            current_node, path = queue.popleft()

            if current_node == goal:
                return path

            if current_node not in visited:
                visited.add(current_node)
                for neighbor in self.graph.get(current_node, []):
                    queue.append((neighbor, path + [neighbor]))

        return None  # Return None if no path is found

    def dfs(self, start, goal):
        # Depth-First Search implementation using recursion
        visited = set() 
        
        def dfs_recursive(current_node, goal, path):
            if current_node == goal:
                return path
            
            visited.add(current_node)
            
            for neighbor in self.graph.get(current_node, []):
                if neighbor not in visited:
                    result_path = dfs_recursive(neighbor, goal, path + [neighbor])
                    if result_path:
                        return result_path
            
            return None

        return dfs_recursive(start, goal, [start])