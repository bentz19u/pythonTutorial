from entities.weighted_directed_graph import WeighedDirectedGraph


# Dijkstra's algorithm
# goal is to find the shortest path (weight wise)
# each edge has a weight, and we should go to destination using the minimum amount of weight

def update_distances(graph, current, distances, parents=None):
    # update the distances of the current node's neighbors
    neighbors = graph.data[current]
    weights = graph.weight[current]
    for i, node in enumerate(neighbors):
        weight = weights[i]
        if distances[current] + weight < distances[node]:
            distances[node] = distances[current] + weight
            if parents:
                parents[node] = current

def pick_next_node(distances, visited):
    # pick the next unvisited node at the smallest distance
    min_distance = float('inf')
    min_node = None
    for node in range(len(distances)):
        if not visited[node] and distances[node] < min_distance:
            min_node = node
            min_distance = distances[node]
    return min_node

def dijkstra_search(graph, source, target):
    visited = [False] * len(graph.data)
    parents = [None] * len(graph.data)
    # inf = infinity
    distances = [float('inf')] * len(graph.data)
    distances[source] = 0
    queue = [source]
    idx = 0

    while idx < len(queue) and not visited[target]:
        # dequeue operation
        current = queue[idx]
        visited[current] = True
        idx += 1

        # update the distances of all the neighbors
        update_distances(graph, current, distances, parents)

        # find the first unvisited node with the smallest distance
        next_node = pick_next_node(distances, visited)
        if next_node:
            queue.append(next_node)

    return distances[target], parents


num_nodes = 6
edges = [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)]

weight_graph = WeighedDirectedGraph(num_nodes, edges, True, True)
print(weight_graph)

result = dijkstra_search(weight_graph, 0, 5)
print(result)