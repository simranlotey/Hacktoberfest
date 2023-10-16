import java.util.Scanner;

public class QuadraticEquationSolver {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the value of a: ");
        double a = scanner.nextDouble();

        System.out.print("Enter the value of b: ");
        double b = scanner.nextDouble();

        System.out.print("Enter the value of c: ");
        double c = scanner.nextDouble();

        // Calculate the discriminant
        double discriminant = b * b - 4 * a * c;

        // Check the discriminant to determine the number of roots
        if (discriminant < 0) {
            System.out.println("The equation has no real roots.");
        } else if (discriminant == 0) {
            System.out.println("The equation has one real root: " + (-b / (2 * a)));
        } else {
            // Calculate the two roots
            double root1 = (-b + Math.sqrt(discriminant)) / (2 * a);
            double root2 = (-b - Math.sqrt(discriminant)) / (2 * a);

            System.out.println("The two roots of the equation are: " + root1 + " and " + root2);
        }
    }
}
