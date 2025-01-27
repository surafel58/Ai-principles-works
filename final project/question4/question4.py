class AdversarialSearch:
    def __init__(self):
        # Representing the state space graph as an adjacency list with utility values
        self.graph = {}
        self.utilities = {}

    def add_edge(self, source, destination):
        if source not in self.graph:
            self.graph[source] = []
        self.graph[source].append(destination)

    def set_utility(self, node, utility):
        self.utilities[node] = utility

    def get_utility(self, node):
        return self.utilities.get(node, None)

    def minimax(self, node, is_maximizing_player):
        # Check if it's a terminal node (leaf with a utility value)
        if node in self.utilities:
            return self.utilities[node], [node]

        # If the node has no children, treat it as a terminal node with utility 0
        if node not in self.graph or not self.graph[node]:
            return 0, [node]

        # Maximizing player's turn
        if is_maximizing_player:
            max_eval = float('-inf')
            best_path = []
            for child in self.graph[node]:
                eval, path = self.minimax(child, False)
                if eval > max_eval:
                    max_eval = eval
                    best_path = [node] + path
            return max_eval, best_path

        # Minimizing player's turn (adversary)
        else:
            min_eval = float('inf')
            best_path = []
            for child in self.graph[node]:
                eval, path = self.minimax(child, True)
                if eval < min_eval:
                    min_eval = eval
                    best_path = [node] + path
            return min_eval, best_path

    def best_path(self, start):
        best_value = float('-inf')
        best_path = []

        for child in self.graph.get(start, []):
            # Adversary's turn next
            value, path = self.minimax(child, False) 
            if value > best_value:
                best_value = value
                best_path = [start] + path

        return best_path, best_value
