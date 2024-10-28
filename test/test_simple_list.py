import unittest

from src.data_structures.list.simple_list import SimpleList


class TestSimpleList(unittest.TestCase):

    def test_initialization(self):
        slist = SimpleList()
        self.assertEqual(len(slist), 0)

    def test_append(self):
        slist = SimpleList()
        slist.append(1)
        self.assertEqual(slist[0], 1)

    def test_insert(self):
        slist = SimpleList()
        slist.append(1)
        slist.insert(0, 2)
        self.assertEqual(slist[0], 2)
        self.assertEqual(slist[1], 1)

    def test_remove(self):
        slist = SimpleList()
        slist.append(1)
        slist.append(2)
        slist.remove(0)
        self.assertEqual(slist[0], 2)

    def test_extend(self):
        slist = SimpleList()
        slist.extend([1, 2, 3])
        self.assertEqual(slist[0], 1)
        self.assertEqual(slist[1], 2)
        self.assertEqual(slist[2], 3)

    def test_clear(self):
        slist = SimpleList()
        slist.extend([1, 2, 3])
        slist.clear()
        self.assertEqual(len(slist), 0)

    def test_count(self):
        slist = SimpleList()
        slist.extend([1, 1, 2, 3, 1])
        self.assertEqual(slist.count(1), 3)

    def test_index_error(self):
        slist = SimpleList()
        slist.append(1)
        with self.assertRaises(IndexError):
            _ = slist[1]
        with self.assertRaises(IndexError):
            slist.insert(2, 2)

    def test_capacity(self):
        slist = SimpleList()
        for i in range(11):
            slist.append(i)
        self.assertTrue(slist.capacity >= 11)


if __name__ == '__main__':
    unittest.main()
