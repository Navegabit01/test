import pprint
from collections import defaultdict


class Graph(object):
    """
    Graph structure
    """
    def __init__(self, connections, directed=False) -> None:
        self._Graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """
        add connection (list of tuple pairs) to graph
        :param connections:
        :return:
        """
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """Add connection between node1 and node2"""
        self._Graph[node2].add(node1)
        if not self._directed:
            self._Graph[node1].add(node2)

    def remove(self, node):
        """Remove all references to the node"""

        for n, cxns in self._Graph.items():
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._Graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        """
        Is node1 is directly connected to node2
        :param node1:
        :param node2:
        :return:
        """
        return node1 in self._Graph and node2 in self._Graph[node1]

    def BFS_SP(self, start=None, goal=None):
        explored = []

        # Queue for traversing the
        # graph in the BFS
        queue = [[start]]

        # If the desired node is
        # reached
        if start == goal:
            print("Same Node")
            return

        # Loop to traverse the graph
        # with the help of the queue
        while queue:
            path = queue.pop(0)
            node = path[-1]

            # Condition to check if the
            # current node is not visited
            if node not in explored:
                neighbours = self._Graph[node]

                # Loop to iterate over the
                # neighbours of the node
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)

                    # Condition to check if the
                    # neighbour node is the goal
                    if neighbour == goal:
                        return new_path
                explored.append(node)
        return

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._Graph))
