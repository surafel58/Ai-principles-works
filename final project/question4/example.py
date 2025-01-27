from question4 import AdversarialSearch

# Example usage
graph = AdversarialSearch()

# Add edges based on figure 4
graph.add_edge("Addis Ababa", "Ambo")
graph.add_edge("Addis Ababa", "Adama") 
graph.add_edge("Addis Ababa", "Buta Jira")
graph.add_edge("Ambo", "Gedo")
graph.add_edge("Ambo", "Nekemte")
graph.add_edge("Gedo", "Shambu")
graph.add_edge("Gedo", "Fincha")
graph.add_edge("Nekemte", "Gimbi")
graph.add_edge("Nekemte", "Limu")
graph.add_edge("Adama", "Dire Dawa")
graph.add_edge("Adama", "Mojo")
graph.add_edge("Buta Jira", "Worabe")
graph.add_edge("Buta Jira", "Wolkite")
graph.add_edge("Worabe", "Hossana")
graph.add_edge("Worabe", "Durame")
graph.add_edge("Dire Dawa", "Harar")
graph.add_edge("Dire Dawa", "Chiro")
graph.add_edge("Wolkite", "Bench Naji")
graph.add_edge("Wolkite", "Tepi")
graph.add_edge("Mojo", "Kaffa")
graph.add_edge("Mojo", "Dilla")

# Set utility values for terminal nodes based on figure 4
graph.set_utility("Shambu", 4)  
graph.set_utility("Fincha", 5)  
graph.set_utility("Gimbi", 8)   
graph.set_utility("Limu", 8)    
graph.set_utility("Harar", 10)  
graph.set_utility("Chiro", 6)   
graph.set_utility("Dilla", 9)   
graph.set_utility("Bench Naji", 5)
graph.set_utility("Kaffa", 7)
graph.set_utility("Tepi", 6) 
graph.set_utility("Durame", 5)
graph.set_utility("Hossana", 6)


# Perform Minimax Search
start_node = "Addis Ababa"
best_path, best_value = graph.best_path(start_node)
print(f"Best path from {start_node} is {best_path} with utility value {best_value}")