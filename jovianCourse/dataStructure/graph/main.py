from jovianCourse.dataStructure.graph.entities.graph import Graph
from jovianCourse.dataStructure.graph.entities.weighted_directed_graph import WeighedDirectedGraph

num_nodes = 5
# edge are two connected nodes, order don't matter
edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
# print(num_nodes, len(edges))

# making an adjacency Lists
graph = Graph(num_nodes, edges)
# print(graph)

# graph.remove_edge(0, 1)
# print(graph)

# graph.add_edge(0, 1)


# print(graph)

# breadth first search, it gives the queue from the `root` given
def bfs(graph, root):
    queue = []
    discovered = [False] * len(graph.data)
    distance = [None] * len(graph.data)
    parent = [None] * len(graph.data)

    discovered[root] = True
    distance[root] = 0
    queue.append(root)
    idx = 0

    while idx < len(queue):
        # dequeue operation
        current = queue[idx]
        idx += 1

        # check all edges of current
        for node in graph.data[current]:
            if not discovered[node]:
                distance[node] = 1 + distance[current]
                parent[node] = current
                discovered[node] = True
                queue.append(node)
    return queue, distance, parent


queue = bfs(graph, 3)
# print(queue)


# depth-first search
def dfs(graph, root):
    result = []
    stack = []
    stack.append(root)
    discovered = [False] * len(graph.data)

    while len(stack) != 0:
        current = stack.pop()
        if not discovered[current]:
            discovered[current] = True
            result.append(current)
            for node in graph.data[current]:
                stack.append(node)

    return result

result = dfs(graph, 3)
# print(result)

# graph with weights
num_nodes5 = 9
edges5 = [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6),
          (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)]


weight_graph = WeighedDirectedGraph(num_nodes5, edges5, False, True)
print(weight_graph)

# graph with directed graph
num_nodes6 = 5
edges6 = [(0, 1), (1, 2), (2, 3), (2, 4), (4, 2), (3, 0)]
directed_graph = WeighedDirectedGraph(num_nodes6, edges6, True, False)
print(directed_graph)