import unittest

from src.data_structures.stack.linkedlist_stack import LinkedListStack


class TestLinkedListStack(unittest.TestCase):

    def test_push(self):
        stack = LinkedListStack()
        stack.push(1)
        self.assertEqual(stack.peek(), 1)

    def test_pop(self):
        stack = LinkedListStack()
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        with self.assertRaises(IndexError):
            stack.pop()

    def test_peek(self):
        stack = LinkedListStack()
        stack.push(3)
        self.assertEqual(stack.peek(), 3)
        stack.pop()
        with self.assertRaises(IndexError):
            stack.peek()

    def test_is_empty(self):
        stack = LinkedListStack()
        self.assertTrue(stack.is_empty())
        stack.push(4)
        self.assertFalse(stack.is_empty())

    def test_size(self):
        stack = LinkedListStack()
        self.assertEqual(stack.size(), 0)
        stack.push(5)
        self.assertEqual(stack.size(), 1)

    def test_clear(self):
        stack = LinkedListStack()
        stack.push(6)
        stack.clear()
        self.assertTrue(stack.is_empty())

    def test_copy(self):
        stack = LinkedListStack()
        stack.push(7)
        stack.push(8)
        stack.push(9)
        copied_stack = stack.copy()
        self.assertEqual(str(stack), str(copied_stack))
        self.assertNotEqual(id(stack), id(copied_stack))

    def test_capacity(self):
        stack = LinkedListStack(capacity=1)
        stack.push(10)
        with self.assertRaises(OverflowError):
            stack.push(11)

    def test_int(self):
        stack = LinkedListStack[int]()
        stack.push(12)
        self.assertEqual(stack.pop(), 12)

    def test_float(self):
        stack = LinkedListStack[float]()
        stack.push(13.1)
        self.assertEqual(stack.pop(), 13.1)

    def test_string(self):
        stack = LinkedListStack[str]()
        stack.push("14.0")
        self.assertEqual(stack.pop(), "14.0")

    def test_custom_object(self):
        class CustomObject:
            def __init__(self, value):
                self.value = value

        obj1 = CustomObject(10)
        obj2 = CustomObject(20)

        stack = LinkedListStack[CustomObject]()
        stack.push(obj1)
        stack.push(obj2)

        self.assertEqual(stack.pop().value, 20)
        self.assertEqual(stack.pop().value, 10)

    def test_multi_data(self):
        stack = LinkedListStack()
        stack.push(15)
        stack.push(16.0)
        stack.push("17.0")
        stack.push([1, 2, 3])
        self.assertEqual(stack.pop(), [1, 2, 3])
        self.assertEqual(stack.pop(), "17.0")
        self.assertEqual(stack.pop(), 16.0)
        self.assertEqual(stack.pop(), 15)


if __name__ == '__main__':
    unittest.main()
