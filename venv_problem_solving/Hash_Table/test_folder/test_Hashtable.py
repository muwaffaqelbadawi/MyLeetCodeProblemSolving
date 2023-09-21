import unittest
import hash_table

myHashTable = hash_table.Hash_Table()

class TestHashtable(unittest.TestCase):
        
    
    def test_add(self):
        key = "Muwaffaq"
        value = "person"
        result = myHashTable.add(key, value)
        self.assertEqual(result, list([key, value]))







if __name__ == "__main__":
    unittest.main()