class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass


# Time Complexity of generating all substring = O(n**3)

def subarray(arr, n):
    # outer loop
    # Pick starting point
    for i in range(0, n):

        # inner loop
        # Pick ending point
        for j in range(i, n):

            # another inner loop
            # Print subarray between current
            # starting and ending point
            for k in range(i, j+1):
                print(arr[k], end=" ")
            print("\n", end="")


# Drivar Program
arr = [1, 2, 3, 4]
n = len(arr)
print("All non-empty subarrays")
subarray(arr, n)
