import unittest

from src.data_structures.linked_list.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_append(self):
        ll = LinkedList[int]()
        ll.append(1)
        ll.append(2)
        self.assertEqual(ll.size(), 2)
        self.assertEqual(ll.get(0), 1)
        self.assertEqual(ll.get(1), 2)

    def test_prepend(self):
        ll = LinkedList[int]()
        ll.prepend(1)
        ll.prepend(2)
        self.assertEqual(ll.size(), 2)
        self.assertEqual(ll.get(0), 2)
        self.assertEqual(ll.get(1), 1)

    def test_insert(self):
        ll = LinkedList[int]()
        ll.append(1)
        ll.append(3)
        ll.insert(1, 2)
        self.assertEqual(ll.size(), 3)
        self.assertEqual(ll.get(1), 2)

    def test_delete(self):
        ll = LinkedList[int]()
        ll.append(1)
        ll.append(2)
        ll.delete(1)
        self.assertEqual(ll.size(), 1)
        self.assertEqual(ll.get(0), 2)

    def test_delete_at(self):
        ll = LinkedList[int]()
        ll.append(1)
        ll.append(2)
        ll.delete_at(0)
        self.assertEqual(ll.size(), 1)
        self.assertEqual(ll.get(0), 2)

    def test_pop(self):
        ll = LinkedList[int]()
        ll.append(1)
        ll.append(2)
        pop_value = ll.pop()
        self.assertEqual(pop_value, 2)
        self.assertEqual(ll.size(), 1)

    def test_find(self):
        ll = LinkedList[int]()
        ll.append(1)
        ll.append(2)
        index = ll.find(2)
        self.assertEqual(index, 1)

    def test_empty(self):
        ll = LinkedList[int]()
        self.assertTrue(ll.is_empty())
        ll.append(1)
        self.assertFalse(ll.is_empty())

    def test_iter(self):
        ll = LinkedList[int]()
        ll.append(1)
        ll.append(2)
        values = [value for value in ll]
        self.assertEqual(values, [1, 2])


if __name__ == '__main__':
    unittest.main()
