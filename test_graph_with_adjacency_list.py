import pytest
from graph_with_adjacency_list import Graph, Node

@pytest.fixture
def sample_graph():
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    return graph

def test_add_node(sample_graph):
    assert 1 in sample_graph.nodes, "Node 1 should be in the graph."
    assert 2 in sample_graph.nodes, "Node 2 should be in the graph."
    assert 3 in sample_graph.nodes, "Node 3 should be in the graph."
    assert 4 not in sample_graph.nodes, "Node 4 should not be in the graph."

def test_add_directed_edge(sample_graph):
    sample_graph.add_edge(1, 2, directed=True)
    assert 2 in sample_graph.nodes[1].adjacencyList, "Node 1 should have an edge to Node 2."
    assert 1 not in sample_graph.nodes[2].adjacencyList, "Node 2 should not have an edge to Node 1."

def test_add_undirected_edge(sample_graph):
    sample_graph.add_edge(2, 3, directed=False)
    assert 3 in sample_graph.nodes[2].adjacencyList, "Node 2 should have an edge to Node 3."
    assert 2 in sample_graph.nodes[3].adjacencyList, "Node 3 should have an edge to Node 2."

def test_edge_on_nonexistent_node(sample_graph, capsys):
    sample_graph.add_edge(1, 4, directed=True)
    captured = capsys.readouterr()
    assert "One or both nodes not found in the graph." in captured.out, \
        "Expected an error message when trying to add an edge with a nonexistent node."
