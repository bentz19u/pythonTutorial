class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def __repr__(self):
        return "\n".join(["{}: {}".format(n,neighbors) for n, neighbors in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()

    def add_edge(self, node1, node2):
        if node2 not in self.data[node1]:
            self.data[node1].append(node2)
        if node1 not in self.data[node2]:
            self.data[node2].append(node1)

    def remove_edge(self, node1, node2):
        if node2 in self.data[node1]:
            self.data[node1].remove(node2)
        if node1 in self.data[node2]:
            self.data[node2].remove(node1)