import java.util.Arrays;
import java.util.Scanner;

public class Median {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Get the length of the list
        System.out.println("Enter the number of elements in the list:");
        int length = scanner.nextInt();

        // Create an array to store the list elements
        int[] list = new int[length];

        // Get the list elements from the user
        System.out.println("Enter the elements:");
        for (int i = 0; i < length; i++) {
            list[i] = scanner.nextInt();
        }

        // Sort the list
        Arrays.sort(list);

        // Find the median
        int median;
        if (length % 2 == 1) {
            // Odd number of elements
            median = list[length / 2];
        } else {
            // Even number of elements
            median = (list[length / 2] + list[length / 2 - 1]) / 2;
        }

        // Print the median
        System.out.println("The median of the list is: " + median);
    }
}
