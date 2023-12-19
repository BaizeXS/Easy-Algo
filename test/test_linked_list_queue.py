import unittest

from internals.data_structures.queue.linked_list_queue import LinkedListQueue


class TestLinkedListQueue(unittest.TestCase):

    def test_initialization(self):
        queue = LinkedListQueue[int]()
        self.assertTrue(queue.is_empty())
        self.assertEqual(len(queue), 0)

    def test_push(self):
        queue = LinkedListQueue[int]()
        queue.push(1)
        queue.push(2)
        self.assertEqual(len(queue), 2)

    def test_pop(self):
        queue = LinkedListQueue[int]()
        queue.push(1)
        queue.push(2)
        self.assertEqual(queue.pop(), 1)
        self.assertEqual(queue.pop(), 2)
        self.assertTrue(queue.is_empty())

    def test_peek(self):
        queue = LinkedListQueue[int]()
        queue.push(1)
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(len(queue), 1)

    def test_is_empty(self):
        queue = LinkedListQueue[int]()
        self.assertTrue(queue.is_empty())
        queue.push(1)
        self.assertFalse(queue.is_empty())

    def test_size(self):
        queue = LinkedListQueue[int]()
        self.assertEqual(queue.size(), 0)
        queue.push(1)
        self.assertEqual(queue.size(), 1)

    def test_clear(self):
        queue = LinkedListQueue[int]()
        queue.push(1)
        queue.clear()
        self.assertTrue(queue.is_empty())

    def test_pop_empty(self):
        queue = LinkedListQueue[int]()
        with self.assertRaises(IndexError):
            queue.pop()

    def test_peek_empty(self):
        queue = LinkedListQueue[int]()
        with self.assertRaises(IndexError):
            queue.peek()

    def test_iteration(self):
        queue = LinkedListQueue[int]()
        numbers = [1, 2, 3]
        for num in numbers:
            queue.push(num)
        for q_val, num in zip(queue, numbers):
            self.assertEqual(q_val, num)


if __name__ == '__main__':
    unittest.main()
