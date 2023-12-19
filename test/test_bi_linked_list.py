import unittest

from internals.data_structures.linked_list.bi_linked_list import BiLinkedList


class TestBiLinkedList(unittest.TestCase):

    def test_initialization(self):
        bll = BiLinkedList()
        self.assertTrue(bll.is_empty())
        self.assertEqual(bll.size(), 0)
        self.assertEqual(str(bll), "")

    def test_append_and_prepend(self):
        bll = BiLinkedList()
        bll.append(1)
        self.assertEqual(bll.get(0), 1)
        bll.prepend(0)
        self.assertEqual(bll.get(0), 0)
        self.assertEqual(len(bll), 2)
        self.assertEqual(bll.size(), 2)

    def test_insert(self):
        bll = BiLinkedList()
        bll.append(1)
        bll.append(3)
        bll.insert(1, 2)
        self.assertEqual(bll.get(1), 2)
        self.assertEqual(len(bll), 3)

    def test_delete(self):
        bll = BiLinkedList()
        bll.append(1)
        bll.append(2)
        bll.append(3)
        bll.delete(2)
        self.assertEqual(bll.find(2), -1)
        self.assertEqual(len(bll), 2)

    def test_delete_at(self):
        bll = BiLinkedList()
        bll.append(1)
        bll.append(2)
        bll.append(3)
        bll.delete_at(1)
        self.assertEqual(bll.get(1), 3)
        self.assertEqual(len(bll), 2)

    def test_pop(self):
        bll = BiLinkedList()
        bll.append(1)
        bll.append(2)
        popped_value = bll.pop()
        self.assertEqual(popped_value, 2)
        self.assertEqual(len(bll), 1)
        popped_value = bll.pop()
        self.assertEqual(popped_value, 1)
        self.assertEqual(len(bll), 0)

    def test_find(self):
        bll = BiLinkedList()
        bll.append(1)
        bll.append(2)
        bll.append(3)
        self.assertEqual(bll.find(2), 1)
        self.assertEqual(bll.find(4), -1)

    def test_get(self):
        bll = BiLinkedList()
        bll.append(1)
        bll.append(2)
        self.assertEqual(bll.get(0), 1)
        self.assertEqual(bll.get(1), 2)

    def test_exceptions(self):
        bll = BiLinkedList()
        with self.assertRaises(IndexError):
            bll.insert(-1, 1)
        with self.assertRaises(IndexError):
            bll.pop()
        with self.assertRaises(IndexError):
            bll.get(0)

    def test_iter(self):
        bll = BiLinkedList()
        values = [1, 2, 3]
        for v in values:
            bll.append(v)
        for i, node in enumerate(bll):
            self.assertEqual(node, values[i])

    def test_str(self):
        bll = BiLinkedList[int]()
        bll.append(1)
        bll.append(2)
        self.assertEqual(str(bll), "1 <-> 2")

    def test_integers(self):
        bll = BiLinkedList[int]()
        bll.append(1)
        bll.append(2)
        self.assertEqual(bll.get(0), 1)
        self.assertEqual(bll.get(1), 2)

    def test_floats(self):
        bll = BiLinkedList[float]()
        bll.append(1.0)
        bll.append(2.0)
        self.assertEqual(bll.get(0), 1.0)
        self.assertEqual(bll.get(1), 2.0)

    def test_strings(self):
        ll = BiLinkedList[str]()
        ll.append("hello")
        ll.append("world")
        self.assertEqual(ll.get(0), "hello")
        self.assertEqual(ll.get(1), "world")

    def test_mixed_types(self):
        ll = BiLinkedList()
        ll.append(1)  # Integer
        ll.append("hello")  # String
        self.assertEqual(ll.get(0), 1)
        self.assertEqual(ll.get(1), "hello")


if __name__ == '__main__':
    unittest.main()
