import unittest
from forTests import *

class Test_SortArray(unittest.TestCase):
    def test_init_1(self):
        array = SortArray()
        self.assertEqual(array._data, [])
        self.assertEqual(array.reverse, False)

    def test_init_2(self):
        array = SortArray([3, 2])
        self.assertEqual(array._data, [2, 3])
        self.assertEqual(array.reverse, False)
    
    def test_init_3(self):
        array = SortArray([3, 2, 1], True)
        self.assertEqual(array._data, [3, 2, 1])
        self.assertEqual(array.reverse, True)

    def test_append(self):
        array = SortArray([])
        array.append(1)
        self.assertEqual(array._data, [1])
        array.append(2)
        self.assertEqual(array._data, [1, 2])
        array.append(0)
        self.assertEqual(array._data, [0, 1, 2])
    
    def test_to_string(self):
        array = SortArray([3, 2, 1, -1, 4, 5])
        self.assertEqual(str(array), '[-1, 1, 2, 3, 4, 5]')
        
    def test_set_reverse(self):
        array = SortArray([3, 2, 1], True)
        self.assertEqual(array._data, [3, 2, 1])
        self.assertEqual(array.reverse, True)
        array.setReverse(False)
        self.assertEqual(array._data, [1, 2, 3])
        self.assertEqual(array.reverse, False)

if __name__ == '__main__':
    unittest.main()