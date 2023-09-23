

# Make it work first then optimize it #

class Solution:
    def __init__(self) -> None:
        # initialize a subArray
        self.subArray = list()
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        # loop through the entire string, Time complexity = O(n)
        for i in range(0, len(s)):
            # if subArray is empty
            if not self.subArray:
            # append the first element to subArray
                self.subArray.append(s[0])
            else:
                # if character happen to be occured before
                if s[i] == s[i-1] and i != len(s)-1:
                    # remove all elements in subArray, Time complexity O(n) approximately
                    self.subArray.clear()
                    # append the current element
                    self.subArray.append(s[i])
                # if there is repeating elements
                elif s[i] in self.subArray:
                    continue
                else:
                    # append element
                    self.subArray.append(s[i])
        print(self.subArray)
        return len(self.subArray)

my_solution = Solution()
print(my_solution.lengthOfLongestSubstring("ckilbkd"))






""" my_list = [1,2,3,4]

for i in range(0, len(my_list)):
    my_list.pop()
    
print(my_list) """