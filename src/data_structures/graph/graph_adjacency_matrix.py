from __future__ import annotations

from typing import TypeVar

T = TypeVar('T')


class GraphAdjacencyMatrix:
    """基于领接矩阵实现的无向图"""

    def __init__(self, vertices: list[T], edges: list[list[int]]):
        # 顶点列表
        self.vertices: list[T] = vertices
        # 领接矩阵
        self.adj_mat: list[list[int]] = []
        # 添加顶点
        for value in vertices:
            self.add_vertex(value)
        # 添加边
        # 请注意，edges 元素代表顶点索引，即对应 vertices 元素索引
        for edge in edges:
            self.add_edge(edge[0], edge[1])

    def size(self) -> int:
        """获取顶点数量"""
        return len(self.vertices)

    def add_vertex(self, value: T):
        """添加顶点"""
        n = self.size()
        # 在顶点列表中添加新的顶点值
        self.vertices.append(value)
        # 在领接矩阵中添加一行
        new_row = [0] * n
        self.adj_mat.append(new_row)
        # 在领接矩阵中添加一列
        for row in self.adj_mat:
            row.append(0)

    def remove_vertex(self, index: int):
        """删除顶点"""
        if index >= self.size():
            raise IndexError("索引越界")
        # 在顶点列表中删除索引 index 的顶点
        self.vertices.pop(index)
        # 在领接矩阵中删除索引 index 的行
        self.adj_mat.pop(index)
        # 在领接矩阵中删除索引 index 的列
        for row in self.adj_mat:
            row.pop(index)

    def add_edge(self, i: int, j: int):
        """添加边"""
        if i < 0 or j < 0 or i >= self.size() or j >= self.size() or i == j:
            raise IndexError("")
        self.adj_mat[i][j] = 1
        self.adj_mat[j][i] = 1

    def remove_edge(self, i: int, j: int):
        """删除边"""
        if i < 0 or j < 0 or i >= self.size() or j >= self.size() or i == j:
            raise IndexError("")
        self.adj_mat[i][j] = 0
        self.adj_mat[j][i] = 0
