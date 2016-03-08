import argparse
import sys


def main(argv):
    parser = argparse.ArgumentParser(
        description='Problem A solution using Dijkstra\'s algorithm')
    parser.add_argument('-i', '--input', metavar='input', nargs=1,
                        help='The input file (default="input.txt")')
    parser.add_argument('-m', '--mode', metavar='mode', nargs=1,
                        help='The mode of the edge construction' +
                             '(default="dr")')

    args = parser.parse_args()
    file_input = "input.txt"
    mode = "dr"
    if args.input:
        file_input = args.input[0]
    if args.mode:
        mode = args.mode[0]
    with open(file_input, 'r') as f:
        graph = Graph(f.read(), mode)
        print(graph.dijkstra())


class Graph(object):
    """
    Implementation of graph for problem A
    Assumptions
    """

    def __init__(self, content, mode):
        """
        Constructor for Graph object; takes a set of string as input as well
        as the construction mode.

        Keyword arguments:
        content -- a String representing a graph. Nodes are separated
                   horizontally by whitespaces and vertically by newlines.
        mode -- determines edge construction of the graph.
                    If "dr": edges are directed downwards and rightwards.
                    If "free": edges extend towards all 4 cardinal directions
        """

        self._vertices = {}
        self._edges = set()

        # construct temp node array for reference when constructing edges
        temp_array = []
        numbering = 0
        for i, line in enumerate(content.split('\n')):
            temp_line = []
            for j, node in enumerate(line.split(' ')):
                numbering += 1
                temp_line.append(numbering)
            temp_array.append(temp_line)

        node_number = 0
        rows = len(content.split('\n'))
        for curr_row, line in enumerate(content.split('\n')):
            cols = len(line.split(' '))
            for curr_col, node in enumerate(line.split(' ')):
                node_number += 1

                # get node number and its weight
                origin_node = str(node_number)
                new_value = int(node, 16)

                # add vertex
                self._vertices[node_number] = new_value

                # start edge construction
                if curr_col + 1 != cols:
                    destination_node = str(node_number + 1)

                    # rightward edge construction
                    self._edges.add((origin_node, destination_node, 'r'))

                    # leftward edge construction
                    if mode == "free":
                        self._edges.add((destination_node, origin_node, 'l'))
                if curr_row + 1 != rows:
                    try:
                        destination_node = str(
                            temp_array[curr_row + 1][curr_col])

                        # downward edge construction
                        self._edges.add((origin_node, destination_node, 'd'))

                        # upward edge construction
                        if mode == "free":
                            self._edges.add(
                                (destination_node, origin_node, 'u'))
                    # For the case of protruding graphs
                    # e.g.
                    # 1 2 3 <-- protruding
                    # 4 5
                    except IndexError:
                        pass

    @property
    def vertices(self):
        return self._vertices

    @property
    def edges(self):
        return self._edges

    def dijkstra(self):
        """Implementation of Dijkstra's algorithm"""
        tentative_nodes = {}
        previous = {}

        # Assign to every node a tentative distance value: set it to zero for
        # our initial node and to infinity for all other nodes.
        # Set the initial node as current. Mark all other nodes unvisited.
        # Create a set of all the unvisited nodes called the unvisited set.
        current = 1
        for i in range(0, len(self._vertices)):
            if i == 0:
                tentative_nodes[i + 1] = 0
            else:
                tentative_nodes[i + 1] = 999999999999999999999999

        # mark the destination node
        destination_node = len(self._vertices)
        path = ',' + str(destination_node)

        # If the destination node has been marked visited, then stop.
        while destination_node in tentative_nodes:
            # For the current node, consider all of its unvisited neighbors and
            # calculate their tentative distances. Compare the newly calculated
            # tentative distance to the current assigned value and assign
            # the smaller one.
            for edge in self._edges:
                # check if current edge has current node as origin
                if str(current) == edge[0] and int(edge[1]) in tentative_nodes:
                    # update tentative distance to the intermediate node
                    tentative_distance = (tentative_nodes[current] +
                                          self._vertices[int(edge[1])])
                    if tentative_distance < tentative_nodes[int(edge[1])]:
                        tentative_nodes[int(edge[1])] = tentative_distance
                        # Mark the node's previous node as current
                        previous[int(edge[1])] = current
            # When we are done considering all of the neighbors of the
            # current node, mark the current node as visited and remove
            # it from the unvisited set.
            tentative_nodes.pop(current)

            # Select the unvisited node that is marked with the smallest
            # tentative distance, set it as the new "current node", and
            # repeat.
            if tentative_nodes:
                current = min(tentative_nodes, key=tentative_nodes.get)

        # Now that we have a minimum path, construct
        backtrack = destination_node
        while backtrack != 1:
            path += ',' + str(previous[backtrack])
            backtrack = previous[backtrack]
        return self.construct_path(path[1:].split(','))

    def construct_path(self, nodes):
        """Algorithm to construct a path from a reversed node input

        Keyword arguments:
        nodes -- a list of strings denoting the least cost path starting from
                 the destination node
        """
        solution = ''
        # reverse the backtrack path
        nodes = list(reversed(nodes))
        for i, node in enumerate(nodes[:-1]):
            for edge in self._edges:
                # find the direction of the edge
                if edge[0] == node and edge[1] == nodes[i + 1]:
                    solution += edge[2] + ','
        return solution[:-1]


if __name__ == "__main__":
    main(sys.argv[1:])
