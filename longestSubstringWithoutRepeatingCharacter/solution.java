package longestSubstringWithoutRepeatingCharacter;

public class solution {
    public static void main(String args[]) {
        int a[] = { 0, 1, 2, 3, 4 };
        int n = a.length;

        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < n - j; j++) {
                for (int k = i; k <= i + j; k++) {
                    System.out.print(a[k]);
                }
                System.out.println();
            }
        }
    }
}