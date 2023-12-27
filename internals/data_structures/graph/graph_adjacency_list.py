from __future__ import annotations

from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class Vertex(Generic[T]):
    """图节点类"""
    def __init__(self, value: T):
        self.value = value


class GraphAdjacencyList:
    """领接表"""
    def __init__(self, edges: list[list[Vertex]]):
        # 领接表
        self.adj_list = dict[Vertex, list[Vertex]]()
        # 添加所有顶点和边
        for edge in edges:
            self.add_vertex(edge[0])
            self.add_vertex(edge[1])
            self.add_edge(edge[0], edge[1])

    def size(self):
        """获取顶点数量"""
        return len(self.adj_list)

    def add_vertex(self, vet: Vertex[T]):
        """添加顶点"""
        if vet in self.adj_list:
            return
        self.adj_list[vet] = []

    def remove_vertex(self, vet: Vertex[T]):
        """删除顶点"""
        if vet not in self.adj_list:
            raise ValueError('')
        # 在领接表中删除顶点 vet 对应的链表
        self.adj_list.pop(vet)
        # 遍历其他顶点的链表，删除所有包含 vet 的边
        for vertex in self.adj_list:
            if vet in self.adj_list[vertex]:
                self.adj_list[vertex].remove(vet)

    def add_edge(self, vet1: Vertex[T], vet2: Vertex[T]):
        """添加边"""
        if vet1 not in self.adj_list or vet2 not in self.adj_list or vet1 == vet2:
            raise ValueError('')
        self.adj_list[vet1].append(vet2)
        self.adj_list[vet2].append(vet1)

    def remove_edge(self, vet1: Vertex[T], vet2: Vertex[T]):
        """删除边"""
        if vet1 not in self.adj_list or vet2 not in self.adj_list or vet1 == vet2:
            raise ValueError
        self.adj_list[vet1].remove(vet2)
        self.adj_list[vet2].remove(vet1)
