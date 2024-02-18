from __future__ import annotations
from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class BiNode:
    """双向链表节点的基类"""

    def __init__(self):
        self.prev: Optional[BiNode] = None
        self.next: Optional[BiNode] = None


class SentinelBiNode(BiNode):
    """哨兵节点类"""

    pass


class BiListNode(BiNode, Generic[T]):
    """双向链表节点类"""

    def __init__(
        self,
        value: T,
        prev_node: Optional[SentinelBiNode | BiListNode[T]] = None,
        next_node: Optional[SentinelBiNode | BiListNode[T]] = None,
    ):
        super().__init__()
        self.value: T = value
        self.prev: Optional[SentinelBiNode | BiListNode[T]] = prev_node
        self.next: Optional[SentinelBiNode | BiListNode[T]] = next_node

    def __repr__(self) -> str:
        return f"BiListNode({self.value})"


def list_to_bi_linked_list():
    pass


def bi_linked_list_to_list():
    pass
