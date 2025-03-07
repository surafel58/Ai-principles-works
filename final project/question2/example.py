from question2 import StateSpaceGraph

# Example usage
graph = StateSpaceGraph()

# Adding edges from Figure 2 with weights
graph.add_edge("Kartum", "Humera", 21)
graph.add_edge("Kartum", "Metema", 19)
graph.add_edge("Metema", "Gondar", 7)
graph.add_edge("Humera", "Shire", 8)
graph.add_edge("Humera", "Gondar", 9)
graph.add_edge("Shire", "Axum", 2)
graph.add_edge("Shire", "Debarke", 9)
graph.add_edge("Debarke", "Gondar", 4)
graph.add_edge("Axum", "Adwa", 1)
graph.add_edge("Axum", "Asmera", 5)
graph.add_edge("Adwa", "Adigrat", 4)
graph.add_edge("Adwa", "Mekelle", 7)
graph.add_edge("Adigrat", "Mekelle", 4)
graph.add_edge("Adigrat", "Asmera", 4)
graph.add_edge("Mekelle", "Sekota", 9)
graph.add_edge("Mekelle", "Alamata", 5)
graph.add_edge("Sekota", "Alamata", 6)
graph.add_edge("Sekota", "Lalibela", 9)
graph.add_edge("Lalibela", "Debre Tabor", 8)
graph.add_edge("Lalibela", "Woldia", 7)
graph.add_edge("Alamata", "Woldia", 3)
graph.add_edge("Alamata", "Samara", 11)
graph.add_edge("Samara", "Woldia", 8)
graph.add_edge("Samara", "Fanti Rasu", 7)
graph.add_edge("Fanti Rasu", "Kilbet Rasu", 6)
graph.add_edge("Debre Tabor", "Bahir Dar", 4)
graph.add_edge("Bahir Dar", "Azezo", 7)
graph.add_edge("Azezo", "Metema", 7)
graph.add_edge("Gondar", "Azezo", 1)
graph.add_edge("Bahir Dar", "Finote Selam", 6)
graph.add_edge("Bahir Dar", "Injibara", 4)
graph.add_edge("Bahir Dar", "Metekel", 11)
graph.add_edge("Injibara", "Finote Selam", 2)
graph.add_edge("Finote Selam", "Debre Markos", 3)
graph.add_edge("Debre Markos", "Debre Sina", 17)
graph.add_edge("Debre Sina", "Debre Birhan", 2)
graph.add_edge("Debre Sina", "Kemise", 6)
graph.add_edge("Kemise", "Dessie", 4)
graph.add_edge("Dessie", "Woldia", 6)
graph.add_edge("Debre Birhan", "Addis Ababa", 5)
graph.add_edge("Addis Ababa", "Ambo", 5)
graph.add_edge("Addis Ababa", "Adama", 3)
graph.add_edge("Adama", "Matahara", 3)
graph.add_edge("Matahara", "Awash", 1)
graph.add_edge("Awash", "Gabi Rasu", 5)
graph.add_edge("Awash", "Chiro", 4)
graph.add_edge("Gabi Rasu", "Samara", 9)
graph.add_edge("Chiro", "Dire Dawa", 8)
graph.add_edge("Dire Dawa", "Harar", 4)
graph.add_edge("Harar", "Babile", 2)
graph.add_edge("Babile", "Jigjiga", 3)
graph.add_edge("Jigjiga", "Dega Habur", 5)
graph.add_edge("Dega Habur", "Kebri Dehar", 6)
graph.add_edge("Kebri Dehar", "Werder", 6)
graph.add_edge("Babile", "Goba", 28)
graph.add_edge("Goba", "Sof Oumer", 6)
graph.add_edge("Goba", "Bale", 18)
graph.add_edge("Sof Oumer", "Bale", 23)
graph.add_edge("Bale", "Liben", 11)
graph.add_edge("Bale", "Dodolla", 13)
graph.add_edge("Sof Oumer", "Goder", 23)
graph.add_edge("Kebri Dehar", "Goder", 5)
graph.add_edge("Gode", "Dollo", 17)
graph.add_edge("Gode", "Mokadisho", 22)
graph.add_edge("Dodolla", "Shashemene", 3)
graph.add_edge("Shashemene", "Hawassa", 1)
graph.add_edge("Hawassa", "Dilla", 3)
graph.add_edge("Dilla", "Bule Hora", 4)
graph.add_edge("Bule Hora", "Yabello", 3)
graph.add_edge("Yabello", "Konso", 3)
graph.add_edge("Konso", "Arba Minch", 4)
graph.add_edge("Arba Minch", "Wolaita Sodo", 4)
graph.add_edge("Wolaita Sodo", "Hossana", 4)
graph.add_edge("Hossana", "Shashemene", 7)
graph.add_edge("Yabello", "Moyale", 6)
graph.add_edge("Moyale", "Nairobi", 22)
graph.add_edge("Arba Minch", "Basketo", 10)
graph.add_edge("Basketo", "Bench Maji", 5)
graph.add_edge("Bench Maji", "Juba", 22)
graph.add_edge("Wolaita Sodo", "Dawaro", 6)
graph.add_edge("Dawaro", "Bonga", 10)
graph.add_edge("Bonga", "Jimma", 4)
graph.add_edge("Bonga", "Mezan Teferi", 4)
graph.add_edge("Bonga", "Tepi", 8)
graph.add_edge("Tepi", "Mezan Teferi", 4)
graph.add_edge("Jimma", "Bedelle", 7)
graph.add_edge("Bedelle", "Nekemte", 4)
graph.add_edge("Nekemte", "Gimbi", 4)
graph.add_edge("Nekemte", "Ambo", 9)
graph.add_edge("Gimbi", "Dembi Dolo", 6)
graph.add_edge("Dembi Dolo", "Assosa", 12)
graph.add_edge("Dembi Dolo", "Gambella", 4)
graph.add_edge("Gambella", "Gore", 5)
graph.add_edge("Gore", "Tepi", 9)
graph.add_edge("Gore", "Bedelle", 6)
graph.add_edge("Jimma", "Wolkite", 8)
graph.add_edge("Wolkite", "Ambo", 6)
graph.add_edge("Wolkite", "Worabe", 5)
graph.add_edge("Hossana", "Worabe", 2)
graph.add_edge("Worabe", "Buta Jirra", 2)
graph.add_edge("Buta Jirra", "Batu", 2)
graph.add_edge("Batu", "Shashemene", 3)
graph.add_edge("Batu", "Adama", 4)
graph.add_edge("Adama", "Assella", 4)
graph.add_edge("Dodolla", "Assasa", 1)


# Perform Uniform Cost Search
start_state = "Addis Ababa"
goal_state = "Lalibela"
multi_goals = ["Axum", "Gondar", "Lalibela", "Babile", "Jimma", "Bale", "Sof Oumer", "Arba Minch"]

ucs_cost, ucs_path = graph.uniform_cost_search(start_state, goal_state)
print("UCS Path to Lalibela:", ucs_path, "with cost:", ucs_cost)

multi_cost, multi_path = graph.multi_goal_ucs(start_state, multi_goals)
print("Multi-Goal UCS Path:", multi_path, "with total cost:", multi_cost)
