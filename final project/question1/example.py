from question1 import StateSpaceGraph

# Initialize the graph
graph = StateSpaceGraph()

# Adding edges from figure 1
graph.add_edge("Kartum", "Humera")
graph.add_edge("Kartum", "Metema")
graph.add_edge("Humera", "Shire")
graph.add_edge("Humera", "Metema")
graph.add_edge("Shire", "Axum")
graph.add_edge("Shire", "Debarke")
graph.add_edge("Debarke", "Gondar")
graph.add_edge("Axum", "Adwa")
graph.add_edge("Adwa", "Adigrat")
graph.add_edge("Adigrat", "Mekelle")
graph.add_edge("Adigrat", "Asmara")
graph.add_edge("Mekelle", "Sekota")
graph.add_edge("Mekelle", "Alamata")
graph.add_edge("Sekota", "Lalibela")
graph.add_edge("Lalibela", "Debre Tabor")
graph.add_edge("Debre Tabor", "Bahir Dar")
graph.add_edge("Bahir Dar", "Azezo")
graph.add_edge("Azezo", "Metema")
graph.add_edge("Bahir Dar", "Finote Selam")
graph.add_edge("Finote Selam", "Debre Markos")
graph.add_edge("Debre Markos", "Debre Sina")
graph.add_edge("Debre Markos", "Injibara")
graph.add_edge("Injibara", "Metekel")
graph.add_edge("Metekel", "Assosa")
graph.add_edge("Assosa", "Gambela")
graph.add_edge("Gambela", "Tepi")
graph.add_edge("Tepi", "Bonga")
graph.add_edge("Tepi", "Mezan Teferi")
graph.add_edge("Bonga", "Jimma")
graph.add_edge("Jimma", "Bedele")
graph.add_edge("Bedele", "Nekemte")
graph.add_edge("Nekemte", "Gimbi")
graph.add_edge("Nekemte", "Ambo")
graph.add_edge("Ambo", "Addis Ababa")
graph.add_edge("Addis Ababa", "Debre Birhan")
graph.add_edge("Debre Birhan", "Kemise")
graph.add_edge("Kemise", "Dessie")
graph.add_edge("Dessie", "Woldia")
graph.add_edge("Woldia", "Alamata")
graph.add_edge("Woldia", "Fanti Rasu")
graph.add_edge("Fanti Rasu", "Kilbet Rasu")
graph.add_edge("Kilbet Rasu", "Samarra")
graph.add_edge("Addis Ababa", "Adama")
graph.add_edge("Adama", "Matahara")
graph.add_edge("Matahara", "Awash")
graph.add_edge("Awash", "Chiro")
graph.add_edge("Chiro", "Dire Dawa")
graph.add_edge("Dire Dawa", "Harar")
graph.add_edge("Harar", "Babile")
graph.add_edge("Babile", "Jijiga")
graph.add_edge("Jijiga", "Degehabur")
graph.add_edge("Degehabur", "Kebri Dehar")
graph.add_edge("Kebri Dehar", "Gode")
graph.add_edge("Gode", "Dollo")
graph.add_edge("Dollo", "Moyale")
graph.add_edge("Moyale", "Yabello")
graph.add_edge("Yabello", "Konso")
graph.add_edge("Konso", "Arba Minch")
graph.add_edge("Arba Minch", "Wolaita Sodo")
graph.add_edge("Wolaita Sodo", "Hossana")
graph.add_edge("Hossana", "Shashemene")
graph.add_edge("Shashemene", "Hawassa")
graph.add_edge("Hawassa", "Dilla")
graph.add_edge("Dilla", "Bule Hora")
graph.add_edge("Bule Hora", "Yabello")
graph.add_edge("Shashemene", "Assasa")
graph.add_edge("Assasa", "Dodola")
graph.add_edge("Dodola", "Goba")
graph.add_edge("Goba", "Bale")
graph.add_edge("Bale", "Liben")
graph.add_edge("Gode", "Liben")
graph.add_edge("Liben", "Sof Oumer")
graph.add_edge("Sof Oumer", "Bale")
graph.add_edge("Sof Oumer", "Goba")
graph.add_edge("Bench Maji", "Basketo")
graph.add_edge("Basketo", "Juba")

# Perform BFS and DFS searches
start_state = "Addis Ababa"
goal_state = "Lalibela"

bfs_path = graph.bfs(start_state, goal_state)
dfs_path = graph.dfs(start_state, goal_state)

print("BFS Path:", bfs_path)
print("DFS Path:", dfs_path) 