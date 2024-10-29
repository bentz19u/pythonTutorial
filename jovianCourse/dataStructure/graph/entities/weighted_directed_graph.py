class WeighedDirectedGraph:
    def __init__(self, num_nodes, edges, directed=False,weighted=False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = weighted
        self.data = [[] for _ in range(num_nodes)]
        self.weight = [[] for _ in range(num_nodes)]
        for edge in edges:
            if self.weighted:
                node1, node2, weight = edge
                self.data[node1].append(node2)
                self.weight[node1].append(weight)
                if not directed:
                    self.data[node2].append(node1)
                    self.weight[node2].append(weight)
            else:
                node1, node2 = edge
                self.data[node1].append(node2)
                if not directed:
                    self.data[node2].append(node1)


    def __repr__(self):
        result = ''
        if self.weighted:
            for i, (nodes, weights) in enumerate(zip(self.data, self.weight)):
                result += "{}: {}\n".format(i, list(zip(nodes, weights)))
        else:
            for i, nodes in enumerate(self.data):
                result += "{}: {}\n".format(i, nodes)

        return result

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