import unittest

from src.data_structures.queue.linked_list_deque import LinkedListDeque


class TestLinkedListDeque(unittest.TestCase):
    def setUp(self):
        self.int_deque = LinkedListDeque[int]()
        self.string_deque = LinkedListDeque[str]()

    def test_push_and_pop(self):
        # 测试添加和删除元素
        self.int_deque.push_first(1)
        self.int_deque.push_last(2)
        self.assertEqual(self.int_deque.pop_first(), 1)
        self.assertEqual(self.int_deque.pop_last(), 2)

        self.string_deque.push_first("hello")
        self.string_deque.push_last("world")
        self.assertEqual(self.string_deque.pop_last(), "world")
        self.assertEqual(self.string_deque.pop_first(), "hello")

    def test_peek(self):
        # 测试查看元素
        self.int_deque.push_first(3)
        self.int_deque.push_last(4)
        self.assertEqual(self.int_deque.peek_first(), 3)
        self.assertEqual(self.int_deque.peek_last(), 4)

        self.string_deque.push_first("test")
        self.string_deque.push_last("deque")
        self.assertEqual(self.string_deque.peek_first(), "test")
        self.assertEqual(self.string_deque.peek_last(), "deque")

    def test_size(self):
        # 测试队列大小
        self.int_deque.push_first(5)
        self.int_deque.push_first(6)
        self.assertEqual(self.int_deque.size(), 2)

        self.string_deque.push_last("size")
        self.string_deque.push_last("test")
        self.assertEqual(self.string_deque.size(), 2)

    def test_is_empty(self):
        # 测试队列是否为空
        self.assertTrue(self.int_deque.is_empty())
        self.int_deque.push_first(7)
        self.assertFalse(self.int_deque.is_empty())
        self.int_deque.pop_first()
        self.assertTrue(self.int_deque.is_empty())

        self.assertTrue(self.string_deque.is_empty())
        self.string_deque.push_last("empty")
        self.assertFalse(self.string_deque.is_empty())
        self.string_deque.pop_last()
        self.assertTrue(self.string_deque.is_empty())

    def test_iteration(self):
        # 测试迭代器
        numbers = [8, 9, 10]
        for num in numbers:
            self.int_deque.push_last(num)
        for i, value in enumerate(self.int_deque):
            self.assertEqual(value, numbers[i])

        words = ["iterate", "over", "deque"]
        for word in words:
            self.string_deque.push_last(word)
        for i, value in enumerate(self.string_deque):
            self.assertEqual(value, words[i])


if __name__ == '__main__':
    unittest.main()
