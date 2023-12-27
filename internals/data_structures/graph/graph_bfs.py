"""广度优先遍历
BFS 通常借助队列来实现。

1. 将遍历起始顶点 startVet 加入队列，并开启循环。
2. 在循环的每轮迭代中，弹出队首顶点并记录访问，然后将该顶点的所有领接顶点加入到队列尾部。
3. 循环步骤 2. ，知道所有顶点被访问完毕后结束。

为了防止重复遍历顶点，我们需要借助一个哈希表 visited 来记录哪些节点已被访问。
"""
from collections import deque

from internals.data_structures.graph.graph_adjacency_list import GraphAdjacencyList, Vertex


def graph_bfs(graph: GraphAdjacencyList, start_vet: Vertex) -> list[Vertex]:
    """广度优先遍历 BFS"""
    res = []
    visited = set[Vertex]([start_vet])
    queue = deque[Vertex]([start_vet])
    while len(queue) > 0:
        vet = queue.popleft()
        res.append(vet)
        for adj_vet in graph.adj_list[vet]:
            if adj_vet in visited:
                continue
            queue.append(adj_vet)
            visited.add(adj_vet)
    return res


