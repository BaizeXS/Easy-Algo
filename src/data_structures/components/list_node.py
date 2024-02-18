from __future__ import annotations
from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class ListNode(Generic[T]):
    """单链表节点类"""

    def __init__(self, value: T, next_node: Optional[ListNode[T]] = None):
        self.value = value
        self.next = next_node


class SentinelNode(ListNode):
    """哨兵节点类"""

    pass


def list_to_linked_list():
    pass


def linked_list_to_list():
    pass
