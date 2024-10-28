import unittest

from src.data_structures.queue.array_deque import ArrayDeque


class TestArrayDeque(unittest.TestCase):
    def setUp(self):
        self.deque = ArrayDeque[int](10)

    def test_push_and_pop(self):
        # 测试在队首和队尾添加和删除元素
        self.deque.push_first(1)
        self.deque.push_last(2)
        self.assertEqual(self.deque.pop_first(), 1)
        self.assertEqual(self.deque.pop_last(), 2)

        # 测试队列自动扩容
        for i in range(10):
            self.deque.push_last(i)
        self.assertEqual(self.deque.size(), 10)
        self.deque.push_last(11)
        self.assertGreater(self.deque.capacity(), 10)  # 容量应该增加

        # 测试队列自动缩容
        for _ in range(6):
            self.deque.pop_last()
        self.assertLess(self.deque.capacity(), 20)  # 容量应该减少

    def test_peek(self):
        # 测试查看元素
        self.deque.push_first(3)
        self.deque.push_last(4)
        self.assertEqual(self.deque.peek_first(), 3)
        self.assertEqual(self.deque.peek_last(), 4)

    def test_clear(self):
        # 测试清空队列
        self.deque.push_first(5)
        self.deque.push_last(6)
        self.deque.clear()
        self.assertTrue(self.deque.is_empty())
        self.assertEqual(self.deque.size(), 0)

    def test_is_empty(self):
        # 测试队列是否为空
        self.assertTrue(self.deque.is_empty())
        self.deque.push_first(7)
        self.assertFalse(self.deque.is_empty())
        self.deque.pop_first()
        self.assertTrue(self.deque.is_empty())

    def test_iteration(self):
        # 测试迭代器
        numbers = [8, 9, 10]
        for num in numbers:
            self.deque.push_last(num)
        for i, value in enumerate(self.deque):
            self.assertEqual(value, numbers[i])


if __name__ == '__main__':
    unittest.main()
