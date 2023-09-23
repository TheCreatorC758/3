import networkx as nx
import matplotlib.pyplot as plt

def best_first_search(graph, start, goal):
    visited = set()
    queue = [(0, start)]

    while queue:
        queue.sort()
        cost, node = queue.pop(0)
        visited.add(node)

        if node == goal:
            return True

        for neighbor, neighbor_cost in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor_cost, neighbor))
                return False

graph = {
    'A': [('B', 6), ('C', 2)],
    'B': [('D', 1)],
    'C': [('D', 8), ('E', 5)],
    'D': [('G', 3)],
    'E': [('G', 4)],
    'G': []
}

start_node = 'A'
goal_node = 'G'

if best_first_search(graph, start_node, goal_node):
    print("Path found")
else:
    print("Path not found")

G = nx.DiGraph()
for node, neighbors in graph.items():
    for neighbor, cost in neighbors:
        G.add_edge(node, neighbor, weight=cost)

pos = nx.spring_layout(G)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()