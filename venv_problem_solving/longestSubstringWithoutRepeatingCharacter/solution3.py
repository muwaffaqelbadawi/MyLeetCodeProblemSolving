# Remeber to communicate with the interviewer while you
# solvoing the problem

"""
    To solve this problem:
    1- generate all the substrings of the given string
    2- Among all substrings having all unique characters
    3- return the maximum length
"""

class Solution:
    def __init__(self, s: str) -> None:
        self.s = s
        self.subArrays = list()
    def subString(self):
        n = len(self.s)
        subArray = list()
        for i in range(0, len(self.s)):
            for j in range(0, n - i):
                for k in range(i, i + j + 1):
                    # print(self.s[k], end=" ")
                    subArray.append(self.s[k])
        self.subArrays.append(subArray)
                # print("\n", end="")
        return self.subArrays
        
my_solution = Solution("abccb")
print(my_solution.subString())

