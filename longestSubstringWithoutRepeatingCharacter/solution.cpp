#include <iostream>
#include <array>

using namespace std;

class Solution
{

public:
    Solution(array<int, 5> arr, int arrSize)
    {
        // This is the constructor function

        for (int i = 0; i < arrSize; i++)
        {
            for (int j = 0; j < arrSize - i; j++)
            {
                for (int k = i; k <= i + j; k++)
                {
                    cout << arr[k];
                }
                cout << endl;
            }
        }
    };
};

int main()
{
    array<int, 5> arr{0, 1, 2, 3, 4};
    int arrSize = arr.size();

    Solution solution1 = Solution(arr, arrSize);
    solution1;
    return 0;
}
