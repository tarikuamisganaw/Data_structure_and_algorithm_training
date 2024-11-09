import pytest
from dfs_and_bfs_implemenation import Graph, dfs, bfs

@pytest.fixture
def sample_graph():
    # Create the graph and add nodes and edges as in the original code
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

    return graph

def test_dfs(sample_graph):
    visited = set()
    path = []
    result = dfs(sample_graph, "New York", "Houston", visited, path)
    assert result is not None, "DFS path should not be None"
    assert "Houston" in result, "DFS path should reach 'Houston'"

def test_bfs(sample_graph):
    result = bfs(sample_graph, "New York", "Houston")
    assert result is not None, "BFS path should not be None"
    assert "Houston" in result, "BFS path should reach 'Houston'"
