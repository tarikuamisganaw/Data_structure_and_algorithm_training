import pytest
from graph_with_adjacency_list import Graph, Node

@pytest.fixture
def sample_graph():
    # Create a new graph instance
    graph = Graph()
    # Add nodes
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    return graph

def test_add_node(sample_graph):
    # Test if nodes are added correctly
    assert 1 in sample_graph.nodes, "Node 1 should be in the graph."
    assert 2 in sample_graph.nodes, "Node 2 should be in the graph."
    assert 3 in sample_graph.nodes, "Node 3 should be in the graph."
    assert 4 not in sample_graph.nodes, "Node 4 should not be in the graph."

def test_add_directed_edge(sample_graph):
    # Add a directed edge from node 1 to node 2
    sample_graph.add_edge(1, 2, directed=True)
    
    # Verify the directed edge is only from node 1 to node 2
    assert 2 in sample_graph.nodes[1].adjacencyList, "Node 1 should have an edge to Node 2."
    assert 1 not in sample_graph.nodes[2].adjacencyList, "Node 2 should not have an edge to Node 1."

def test_add_undirected_edge(sample_graph):
    # Add an undirected edge between node 2 and node 3
    sample_graph.add_edge(2, 3, directed=False)
    
    # Verify that both nodes have edges to each other
    assert 3 in sample_graph.nodes[2].adjacencyList, "Node 2 should have an edge to Node 3."
    assert 2 in sample_graph.nodes[3].adjacencyList, "Node 3 should have an edge to Node 2."

def test_edge_on_nonexistent_node(sample_graph, capsys):
    # Try to add an edge where one or both nodes don't exist
    sample_graph.add_edge(1, 4, directed=True)
    
    # Capture the output and check for the correct error message
    captured = capsys.readouterr()
    assert "One or both nodes not found in the graph." in captured.out, \
        "Expected an error message when trying to add an edge with a nonexistent node."
