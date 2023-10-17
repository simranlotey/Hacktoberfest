import java.util.Arrays;

public class anagram_detector {

    public static boolean areAnagrams(String word1, String word2) {
        String cleanWord1 = word1.replaceAll("\\s", "").toLowerCase();
        String cleanWord2 = word2.replaceAll("\\s", "").toLowerCase();

        if (cleanWord1.length() != cleanWord2.length()) {
            return false;
        }

        char[] word1Array = cleanWord1.toCharArray();
        char[] word2Array = cleanWord2.toCharArray();

        Arrays.sort(word1Array);
        Arrays.sort(word2Array);

        return Arrays.equals(word1Array, word2Array);
    }

    public static void main(String[] args) {
        String word1 = "listen";

        String word2 = "silent";

        if (areAnagrams(word1, word2)) {
            System.out.println(word1 + " and " + word2 + " are anagrams.");
        } else {
            System.out.println(word1 + " and " + word2 + " are not anagrams.");
        }
    }
}