import unittest
from hash_table import add, lookup


class TestHashtable(unittest.TestCase):
    """ def test_add(self):
        key1, value1 = "Muwaffaq", "Author"
        key2, value2 = "Alice", "Girl"
        key3, value3 = "Seri", "Personal Assistant"
        
        self.assertEqual(add(key1, value1), list([key1, value1]))
        self.assertEqual(add(key2, value2), list([key2, value2]))
        self.assertEqual(add(key3, value3), list([key3, value3])) """
        
    def test_lookup(self):
        key1 = "Muwaffaq"
        key2 = "Alice"
        key3 = "Seri"
        
        self.assertEqual(lookup(key1), None)
        self.assertEqual(lookup(key2), None)
        self.assertEqual(lookup(key3), None)




if __name__ == "__main__":
    unittest.main()