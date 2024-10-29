from jovianCourse.dataStructure.graph.adjacency_list.entities.graph import Graph

num_nodes = 5
# edge are two connected nodes, order don't matter
edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
# print(num_nodes, len(edges))

# making an adjacency Lists
graph = Graph(num_nodes, edges)
print(graph)

graph.remove_edge(0, 1)
print(graph)

graph.add_edge(0, 1)
print(graph)