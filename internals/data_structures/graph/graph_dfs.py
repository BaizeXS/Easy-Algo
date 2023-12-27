"""深度优先遍历

"""
from internals.data_structures.graph.graph_adjacency_list import GraphAdjacencyList, Vertex


def dfs(graph: GraphAdjacencyList, visited: set[Vertex], res: list[Vertex], start_vet: Vertex):
    """深度优先遍历辅助函数"""
    res.append(start_vet)
    visited.add(start_vet)
    for adj_vet in graph[start_vet]:
        if adj_vet in visited:
            continue
        dfs(graph, visited, res, adj_vet)


def graph_dfs(graph: GraphAdjacencyList, start_vet: Vertex) -> list[Vertex]:
    """深度优先遍历"""
    res = []
    visited = set[Vertex]()
    dfs(graph, visited, res, start_vet)
    return res

