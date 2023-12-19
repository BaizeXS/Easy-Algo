import unittest

from internals.data_structures.queue.array_queue import ArrayQueue


class TestArrayQueue(unittest.TestCase):

    def test_initialization(self):
        queue = ArrayQueue[int](5)
        self.assertEqual(queue.capacity(), 5)
        self.assertTrue(queue.is_empty())

    def test_push_and_pop(self):
        queue = ArrayQueue[int]()
        queue.push(1)
        queue.push(2)
        self.assertEqual(queue.pop(), 1)
        self.assertEqual(queue.pop(), 2)

    def test_peek(self):
        queue = ArrayQueue[str]()
        queue.push("hello")
        queue.push("world")
        self.assertEqual(queue.peek(), "hello")
        self.assertEqual(queue.size(), 2)

    def test_is_empty(self):
        queue = ArrayQueue[float]()
        self.assertTrue(queue.is_empty())
        queue.push(1.1)
        self.assertFalse(queue.is_empty())

    def test_clear(self):
        queue = ArrayQueue[int]()
        for i in range(5):
            queue.push(i)
        queue.clear()
        self.assertTrue(queue.is_empty())

    def test_pop_empty(self):
        queue = ArrayQueue[int]()
        with self.assertRaises(IndexError):
            queue.pop()

    def test_peek_empty(self):
        queue = ArrayQueue[int]()
        with self.assertRaises(IndexError):
            queue.peek()

    def test_iteration(self):
        queue = ArrayQueue[int]()
        for i in range(5):
            queue.push(i)
        for i, item in enumerate(queue):
            self.assertEqual(item, i)

    def test_resize(self):
        queue = ArrayQueue[int](2)
        queue.push(1)
        queue.push(2)
        self.assertEqual(queue.capacity(), 2)
        queue.push(3)
        self.assertGreater(queue.capacity(), 2)  # 队列应该自动扩容


if __name__ == '__main__':
    unittest.main()
