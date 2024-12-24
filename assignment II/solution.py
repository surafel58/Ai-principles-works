import networkx as nx
from collections import deque
import matplotlib.pyplot as plt

# Global visited set to track visited nodes
visited = set()
def visualize_graph(cities, roads, strategy=None, start_city=None, goal_city=None):
    """
    Parameters:
    - cities: List of city names.
    - roads: Dictionary with city connections as {city: [(connected_city, distance)]}.
    - strategy: Optional search strategy ('bfs', 'dfs', or 'weighted_bfs')
    - start_city: Optional starting city for path visualization
    - goal_city: Optional goal city for path visualization
    
    Creates and displays a visualization of the road network using networkx.
    If strategy is provided, also visualizes the found path.
    """
    # Create directed graph
    G = nx.Graph()
    
    # Add edges with weights
    for city, connections in roads.items():
        for connected_city, distance in connections:
            G.add_edge(city, connected_city, weight=distance)
    
    # Set up the plot
    pos = nx.circular_layout(G)
    plt.figure(figsize=(12, 8))
    
    # Draw the base graph with different colors for start/goal cities
    node_colors = []
    for node in G.nodes():
        if node == start_city:
            node_colors.append('lightgreen')  # Start city in green
        elif node == goal_city:
            node_colors.append('lightpink')   # Goal city in pink
        else:
            node_colors.append('lightblue')   # Other cities in blue
            
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    
    # If strategy is provided, visualize the path
    if strategy and start_city and goal_city:
        path, cost = uninformed_path_finder(cities, roads, start_city, goal_city, strategy)
        if path:
            path_edges = list(zip(path[:-1], path[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)
            plt.title(f"{strategy.upper()} Path - Total Cost: {cost}km")
        else:
            plt.title(f"No path found using {strategy.upper()}")
    else:
        plt.title("Road Network Visualization")
    
    plt.axis('off')
    plt.show()

def uninformed_path_finder(cities, roads, start_city, goal_city, strategy):
    """
    Parameters:
    - cities: List of city names.
    - roads: Dictionary with city connections as {city: [(connected_city, distance)]}.
    - start_city: The city to start the journey.
    - goal_city: The destination city (for specific tasks).
    - strategy: The uninformed search strategy to use ('bfs' or 'dfs').
    
    Returns:
    - path: List of cities representing the path from start_city to goal_city.
    - cost: Total cost (number of steps or distance) of the path.
    """
    # Reset visited set for each new search
    visited.clear()
    
    if strategy == 'bfs':
        return bfs(cities, roads, start_city, goal_city)
    elif strategy == 'dfs':
        return dfs(cities, roads, start_city, goal_city)
    elif strategy == 'weighted_bfs':
        return weighted_bfs(cities, roads, start_city, goal_city)
    else:
        raise ValueError("Invalid strategy. Must be 'bfs', 'dfs', or 'weighted_bfs'")

def traverse_all_cities(cities, roads, start_city, strategy):
    """
    Parameters:
    - cities: List of city names.
    - roads: Dictionary with city connections as {city: [(connected_city, distance)]}.
    - start_city: The city to start the journey.
    - strategy: The uninformed search strategy to use ('bfs' or 'dfs').
    
    Returns:
    - paths_with_costs: List of tuples containing (path, cost) for each goal city
    """
    paths_with_costs = []
    
    # Get paths to all other cities using the specified strategy
    for goal_city in cities:
        if goal_city != start_city:
            path, cost = uninformed_path_finder(cities, roads, start_city, goal_city, strategy)
            if path:
                paths_with_costs.append((path, cost))
                print(f"{strategy.upper()} Path from {start_city} to {goal_city}:")
                print(f"Path: {' -> '.join(path)}")
                print(f"Cost: {cost}km\n")
            else:
                print(f"No path found from {start_city} to {goal_city}\n")
                
    return paths_with_costs

def bfs(cities, roads, start_city, goal_city=None):
    """
    Performs Breadth-First Search on the road network.
    
    Parameters:
    - cities: List of city names
    - roads: Dictionary with city connections
    - start_city: Starting city for the search
    - goal_city: Optional goal city to search for
    
    Returns:
    - path: List of cities in the path found
    - cost: Total cost/distance of the path
    """
    # Handle start city equals goal city case
    if start_city == goal_city:
        return ([start_city], 0)

    # Initialize queue and path tracking
    queue = deque([start_city])
    paths = {start_city: (None, 0)}
    
    # BFS traversal
    while queue:
        current = queue.popleft()
        visited.add(current)
        
        # Check if goal is reached
        if current == goal_city:
            break
            
        # Add unvisited neighbors to queue
        for next_city, cost in roads[current]:
            if next_city not in visited and next_city not in paths:
                queue.append(next_city)
                paths[next_city] = (current, cost)
    
    # Goal not found
    if goal_city not in paths:
        return (None, 0)
        
    # Reconstruct path
    path = []
    total_cost = 0
    current = goal_city
    
    while current:
        path.append(current)
        prev, cost = paths[current]
        total_cost += cost
        current = prev
        
    return (path[::-1], total_cost)


def dfs(cities, roads, start_city, goal_city=None):
    """
    Performs Depth-First Search on the road network.
    
    Parameters:
    - cities: List of city names
    - roads: Dictionary with city connections 
    - start_city: Starting city for the search
    - goal_city: Optional goal city to search for
    
    Returns:
    - path: List of cities in the path found
    - cost: Total cost/distance of the path
    """

    visited.add(start_city)
    curr_path = [start_city]
    curr_cost = 0

    if start_city == goal_city:
        return (curr_path, curr_cost)

    for city in roads[start_city]:
        if not city[0] in visited:
            path, cost = dfs(cities, roads, city[0], goal_city)
            if path:
                curr_path += path
                curr_cost += (city[1] + cost)
                return (curr_path, curr_cost)
    
    return (None, 0)

def weighted_bfs(cities, roads, start_city, goal_city=None):
    """
    Performs Breadth-First Search considering road distances/weights.
    
    Parameters:
    - cities: List of city names
    - roads: Dictionary with city connections and distances
    - start_city: Starting city for the search
    - goal_city: Optional goal city to search for
    
    Returns:
    - path: List of cities in the path found
    - cost: Total distance/weight of the path
    """
    # Handle start = goal case
    if start_city == goal_city:
        return ([start_city], 0)

    # Track shortest paths and costs
    paths = {start_city: (None, 0)}
    queue = deque([start_city])

    # BFS traversal tracking costs
    while queue:
        current = queue.popleft()
        visited.add(current)
        cost_to_current = paths[current][1]

        for next_city, step_cost in roads[current]:
            cost_to_next = cost_to_current + step_cost
            
            # Add or update path if shorter
            if next_city not in paths or cost_to_next < paths[next_city][1]:
                paths[next_city] = (current, cost_to_next)
                if next_city not in visited:
                    queue.append(next_city)

    # Goal not found
    if goal_city not in paths:
        return (None, 0)

    # Reconstruct path
    path = []
    current = goal_city
    while current:
        path.append(current)
        current = paths[current][0]

    return (path[::-1], paths[goal_city][1])


cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle', 'Dire Dawa', 'Jimma', 'Dessie', 'Jijiga']
roads = {
    'Addis Ababa': [('Hawassa', 275), ('Bahir Dar', 510), ('Dire Dawa', 450), ('Jimma', 350)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180), ('Dessie', 300)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300), ('Dessie', 360)],
    'Hawassa': [('Mekelle', 1000), ('Addis Ababa', 275), ('Dire Dawa', 600)],
    'Mekelle': [('Gondar', 300), ('Hawassa', 1000), ('Dessie', 400)],
    'Dire Dawa': [('Addis Ababa', 450), ('Hawassa', 600), ('Jijiga', 150)],
    'Jimma': [('Addis Ababa', 350), ('Hawassa', 400)],
    'Dessie': [('Bahir Dar', 300), ('Gondar', 360), ('Mekelle', 400)],
    'Jijiga': [('Dire Dawa', 150)]
}

def main():
    print("\nSelect search mode:")
    print("1. Find path between two cities")
    print("2. Find paths from start city to all cities")
    
    while True:
        mode = input("\nSelect mode (1-2) or 'q' to quit: ")
        
        if mode.lower() == 'q':
            break
            
        if mode not in ['1', '2']:
            print("Invalid choice. Please select 1 or 2")
            continue
            
        print("\nAvailable search strategies:")
        print("1. BFS (Breadth-First Search)")
        print("2. DFS (Depth-First Search)") 
        print("3. Weighted BFS")
        
        choice = input("\nSelect a search strategy (1-3): ")
        if choice not in ['1', '2', '3']:
            print("Invalid choice. Please select 1, 2, or 3")
            continue
            
        strategy_map = {
            '1': 'bfs',
            '2': 'dfs', 
            '3': 'weighted_bfs'
        }
        
        strategy = strategy_map[choice]
        
        print("\nAvailable cities:", ', '.join(cities))
        start = input("Enter start city: ")
        
        if start not in cities:
            print("Invalid start city. Please try again.")
            continue
            
        if mode == '1':
            goal = input("Enter goal city: ")
            if goal not in cities:
                print("Invalid goal city. Please try again.")
                continue
                
            # Find and display path
            path, cost = uninformed_path_finder(cities, roads, start, goal, strategy)
            print(f"\n{strategy.upper()} Results:")
            if path:
                print(f"Path: {' -> '.join(path)}")
                print(f"Total distance: {cost}km")
            else:
                print("No path found!")
                
            # Visualize
            visualize = input("\nWould you like to visualize the path? (y/n): ")
            if visualize.lower() == 'y':
                visualize_graph(cities, roads, strategy, start, goal)
                
        else:
            # Find paths to all cities
            traverse_all_cities(cities, roads, start, strategy)
            
            # Visualize
            visualize = input("\nWould you like to visualize the network? (y/n): ")
            if visualize.lower() == 'y':
                visualize_graph(cities, roads)

if __name__ == "__main__":
    main()
