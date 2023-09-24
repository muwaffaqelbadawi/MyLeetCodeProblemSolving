import unittest
import solution2

# print(sys.path)

class TestLengthOfLongestSubstring(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        test = solution2.my_solution.lengthOfLongestSubstring
        
        self.assertEqual(test("abcabcbb"), 3)
        self.assertEqual(test("bbbbb"), 1)
        self.assertEqual(test("pwwkew"), 3)
        self.assertEqual(test("ckilbkd"), 5)
        self.assertEqual(test("anviaj"), 5)
        
# Test Cases:
        # abcabcbb, 3
        # bbbbb, 1
        # pwwkew, 3
        # ckilbkd, 5
        
if __name__ == "__main__":
    unittest.main()