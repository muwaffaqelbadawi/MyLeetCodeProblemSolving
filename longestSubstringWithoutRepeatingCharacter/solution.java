package longestSubstringWithoutRepeatingCharacter;

public class solution {
    public static void main(String args[]) {
        // This is the constructor function

        int arr[] = { 0, 1, 2, 3, 4 };
        int arrSize = arr.length;

        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arrSize - j; j++) {
                for (int k = i; k <= i + j; k++) {
                    System.out.print(arr[k]);
                }
                System.out.println();
            }
        }
    }
}