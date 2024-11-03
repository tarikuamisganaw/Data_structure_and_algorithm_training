from collections import deque

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
        directed (bool): check Whether the edge is directed or undirected.
        """
        if val1 in self.nodes and val2 in self.nodes:
            node1 = self.nodes[val1]
            node2 = self.nodes[val2]
            
            if directed:
                node1.add_edge(node2)
            else:
                node1.add_edge(node2)
                node2.add_edge(node1)
        else:
            print("One or both nodes not found in the graph.")

def dfs(graph, start, end, visited, path):
    """
    Perform Depth-First Search (DFS) to find a path from start to end.

    Parameters:
    graph (Graph): The graph to search.
    start: The starting node value.
    end: The ending node value.
    visited (set): A set of visited nodes.
    path (list): The current path being explored.

    Returns:
    list: The path from start to end, or None if no path exists.
    """
    visited.add(start)
    path.append(start)

    if start == end:
        return path

    for nei in graph.nodes[start].adjacencyList.values():
        if nei.val not in visited:
            res = dfs(graph, nei.val, end, visited, path)
            if res:
                return res

    path.pop()  # Backtrack if no path found
    return None

def bfs(graph, start, end):
    """
    Perform Breadth-First Search (BFS) to find a path from start to end.

    Parameters:
    graph (Graph): The graph to search.
    start: The starting node value.
    end: The ending node value.

    Returns:
    list: The path from start to end, or an empty list if no path exists.
    """
    visited = set()
    path = []
    queue = deque([start])
    parent = {start: None}

    while queue:
        node = queue.popleft()
        visited.add(node)

        if node == end:
            break

        for nei in graph.nodes[node].adjacencyList.values():
            if nei.val not in visited:
                visited.add(nei.val)
                queue.append(nei.val)
                parent[nei.val] = node

    if end not in parent:
        return []  # No path found

    while end is not None:
        path.append(end)
        end = parent[end]

    path.reverse()  # Reverse the path to get it from start to end
    return path 

# Create the graph and add nodes and edges
graph = Graph()
cities = ["New York", "Los Angeles", "Chicago", "Houston", "San Francisco",
          "Seattle", "Boston", "Miami"]

# Insert each city as a node in the graph
for val in cities:
    graph.add_node(val)

# Add edges between pairs of cities
graph.add_edge("New York", "Los Angeles", directed=False)
graph.add_edge("New York", "Chicago", directed=False)
graph.add_edge("New York", "Houston", directed=False)
graph.add_edge("Los Angeles", "Chicago", directed=False)
graph.add_edge("Los Angeles", "Houston", directed=False)
graph.add_edge("Chicago", "Houston", directed=False)
graph.add_edge("San Francisco", "Los Angeles", directed=False)
graph.add_edge("San Francisco", "Chicago", directed=False)
graph.add_edge("San Francisco", "Houston", directed=False)
graph.add_edge("Seattle", "Los Angeles", directed=False)
graph.add_edge("Seattle", "Chicago", directed=False)
graph.add_edge("Seattle", "Houston", directed=False)
graph.add_edge("Boston", "Los Angeles", directed=False)
graph.add_edge("Boston", "Chicago", directed=False)
graph.add_edge("Boston", "Houston", directed=False)
graph.add_edge("Miami", "Los Angeles", directed=False)
graph.add_edge("Miami", "Chicago", directed=False)
graph.add_edge("Miami", "Houston", directed=False)

# Define start and end cities
start = "New York"
end = "Houston"
visited = set()
path = []

# Test the DFS and BFS paths between two cities
dfs_path = dfs(graph, start, end, visited, path)
bfs_path = bfs(graph, start, end)

print("DFS path:", " -> ".join(dfs_path) if dfs_path else "No path found")
print("BFS path:", " -> ".join(bfs_path) if bfs_path else "No path found")