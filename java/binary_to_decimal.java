import java.util.Scanner;

public class BinaryToDecimal {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter a binary number: ");
        String binaryNumber = scanner.nextLine();

        int decimalNumber = 0;
        int power = 0;

        for (int i = binaryNumber.length() - 1; i >= 0; i--) {
            int digit = binaryNumber.charAt(i) - '0';
            decimalNumber += digit * Math.pow(2, power);
            power++;
        }

        System.out.println("The decimal equivalent of the binary number is: " + decimalNumber);
    }
}
