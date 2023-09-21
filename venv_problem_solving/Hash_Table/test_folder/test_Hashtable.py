import unittest
import hash_table


myHashTable = hash_table.Hash_Table()



class TestHashtable(unittest.TestCase):
    def test_add(self):
        result = myHashTable.add("muwaffaq", "person")
        self.assertEqual(result, None)









if __name__ == "__main__":
    unittest.main()        