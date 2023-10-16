import java.util.Scanner;

public class CountOccurrencesOfChar {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        
        System.out.println("Enter a text: ");
        String text = scanner.nextLine();

        
        System.out.println("Enter the character to count: ");
        char character = scanner.next().charAt(0);

        
        int count = 0;
        for (int i = 0; i < text.length(); i++) {
            if (text.charAt(i) == character) {
                count++;
            }
        }

        
        System.out.println("The number of occurrences of the character '" + character + "' in the text is: " + count);
    }
}
