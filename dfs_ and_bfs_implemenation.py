from collections import deque

class Node:
    def __init__(self, value):
        self.val = value
        self.adjacencyList = {}

    def add_edge(self, node):
        if node.val not in self.adjacencyList:
            self.adjacencyList[node.val] = node

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value):
        if value not in self.nodes:
            new_node = Node(value)
            self.nodes[value] = new_node

    def add_edge(self, val1, val2, directed=True):
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
    visited.add(start)
    path.append(start)

    if start == end:
        return path

    for nei in graph.nodes[start].adjacencyList.values():
        if nei.val not in visited:
            res = dfs(graph, nei.val, end, visited, path)
            if res:
                return res

    path.pop()
    return None

def bfs(graph, start, end):
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
        return []

    while end is not None:
        path.append(end)
        end = parent[end]

    path.reverse()
    return path 


def test_dfs_and_bfs():
    graph = Graph()
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "San Francisco",
              "Seattle", "Boston", "Miami"]

    for val in cities:
        graph.add_node(val)

    edges = [
        ("New York", "Los Angeles"), ("New York", "Chicago"), ("New York", "Houston"),
        ("Los Angeles", "Chicago"), ("Los Angeles", "Houston"), ("Chicago", "Houston"),
        ("San Francisco", "Los Angeles"), ("San Francisco", "Chicago"),
        ("San Francisco", "Houston"), ("Seattle", "Los Angeles"),
        ("Seattle", "Chicago"), ("Seattle", "Houston"), ("Boston", "Los Angeles"),
        ("Boston", "Chicago"), ("Boston", "Houston"), ("Miami", "Los Angeles"),
        ("Miami", "Chicago"), ("Miami", "Houston")
    ]
    for val1, val2 in edges:
        graph.add_edge(val1, val2, directed=False)

    # Test DFS
    visited = set()
    path = []
    dfs_path = dfs(graph, "New York", "Houston", visited, path)
    assert dfs_path is not None, "DFS should find a path"
    assert "Houston" in dfs_path, "DFS path should reach 'Houston'"

    # Test BFS
    bfs_path = bfs(graph, "New York", "Houston")
    assert bfs_path is not None, "BFS should find a path"
    assert "Houston" in bfs_path, "BFS path should reach 'Houston'"


if __name__ == "__main__":
    test_dfs_and_bfs()
    print("All tests passed!")
