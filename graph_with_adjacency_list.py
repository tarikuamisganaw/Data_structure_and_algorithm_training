class Node:
    def __init__(self, value):
        """
        Initialize a node with a value and an adjacency list.

        Parameters:
        value: The value of the node.
        """
        self.val = value
        self.adjacencyList = {}

    def add_edge(self, node):
        """
        Add an edge to the node.

        Parameters:
        node (Node): The node to connect with this node.
        """
        if node.val not in self.adjacencyList:
            self.adjacencyList[node.val] = node

class Graph:
    def __init__(self):
        """Initialize an empty graph with a dictionary of nodes."""
        self.nodes = {}

    def add_node(self, value):
        """
        Add a node to the graph.

        Parameters:
        value: The value of the node to add.
        """
        if value not in self.nodes:
            new_node = Node(value)
            self.nodes[value] = new_node

    def add_edge(self, val1, val2, directed=True):
        """
        Add an edge between two nodes in the graph.

        Parameters:
        val1: The value of the first node.
        val2: The value of the second node.
        directed (bool): Whether the edge is directed or undirected.
        """
        if val1 in self.nodes and val2 in self.nodes:
            node1 = self.nodes[val1]
            node2 = self.nodes[val2]
            
            if directed:
                node1.add_edge(node2)
                print(f"Directed edge added from {node1.val} to {node2.val}.")
            else:
                node1.add_edge(node2)
                node2.add_edge(node1)
                print(f"Undirected edge added between {node1.val} and {node2.val}.")
        else:
            print("One or both nodes not found in the graph.")

#Test graph implementation
graph = Graph() 
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_edge(1, 2, directed=True)
graph.add_edge(2, 3, directed=False)