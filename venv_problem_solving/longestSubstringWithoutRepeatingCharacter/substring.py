# Time Complexity of generating all substring = O(n**3)
class Solution:
    def __init__(self) -> None:
        # This is the constructor function
        pass

    def subarray(self, arr, listSize):
        for i in range(0, listSize):
            for j in range(0, listSize - i):
                for k in range(i, i + j + 1):
                    print(arr[k], end=" ")
                print("\n", end="")


# Drivar Program
arr = "abcabcbb"
# arr = [0, 1, 2, 3, 4]
listSize = len(arr)

solution1 = Solution()
solution1.subarray(arr, listSize)
